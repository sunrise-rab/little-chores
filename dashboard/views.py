from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from tasks.models import AGE_GROUP_CHOICES
from django.contrib import messages
from .models import Child
from .forms import ChildForm
from tasks.models import Task
from .forms import AssignChoresForm
from .models import AssignedTask
from django.db.models import F 
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.db.models import Q
from django.views.decorators.http import require_POST




# Create your views here.

def dashboard(request):
    """
    Display the main dashboard for the logged-in parent.
   
    **Context**
   ``children``
    A queryset of :model:`dashboard.Child` objects belonging to the logged-in parent.

    **Template:**
    :template:`dashboard/dashboard.html`
    """  
    children = (
        Child.objects
        .filter(parent=request.user)
        .annotate(
            total_stars=Coalesce(
                Sum(
                    "assigned_tasks__stickers_awarded",
                    filter=Q(assigned_tasks__status="done"),
                ),
                0,
            )
        )
    )

    return render(request, "dashboard/dashboard.html", {"children": children})
    

def add_child(request):
    if request.method == "POST":
        child_form = ChildForm(request.POST)
        if child_form.is_valid():
            child = child_form.save(commit=False)
            child.parent = request.user
            child.save()
            messages.add_message(
            request, messages.SUCCESS,
            'A child  has been added successfully '
          )
            return redirect("dashboard:dashboard")
    else:
        child_form = ChildForm()
        

    return render(
        request, 
        "dashboard/add_child.html",
         {"child_form": child_form}
         )

def edit_child(request, pk):
    """
    Allows a parent to edit an existing child.
    Only the child's parent can edit.
    """
    child = get_object_or_404(Child, pk=pk, parent=request.user)

    if request.method == "POST":
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            messages.add_message(
            request, messages.SUCCESS,
           'Child details has been edited successfully '
    )
            return redirect("dashboard:dashboard")
    else:
        form = ChildForm(instance=child)

    return render(request, "dashboard/edit_child.html", {
        "form": form,
        "child": child
    })



def delete_child(request, pk):
    """
    Allows a parent to delete a child after confirmation.
    """
    child = get_object_or_404(Child, pk=pk, parent=request.user)

    if request.method == "POST":
        child.delete()
        messages.add_message(
        request, messages.SUCCESS,
        'Child has been deleted successfully ')
        
        return redirect("dashboard:dashboard")

    return render(request, "dashboard/delete_child.html", {
        "child": child
    })



def assign_tasks(request):
    # Get age_appropriate chores
    form = AssignChoresForm(request.GET or None, user=request.user)

    if request.method == "POST":
        form = AssignChoresForm(request.POST, user=request.user)
        if form.is_valid():
            child = form.cleaned_data["child"]
            chores = form.cleaned_data["chores"]

            for task in chores:
                AssignedTask.objects.create(child=child, task=task)
            messages.add_message(
            request, messages.SUCCESS,
           'Chores has been assigned successefully ')
            return redirect("dashboard:dashboard")

    return render(request, "dashboard/assign_tasks.html", {"form": form})
   
def todo_completed(request):
    """
    Display assigned chores for the logged-in parent, grouped by status.

    This view separates chores into two sections:
    - To do
    - Completed

    **Context**

    ``todo_tasks``
    A queryset of :model:`dashboard.AssignedTask` objects with status ``"todo"``.

    ``done_tasks``
    A queryset of :model:`dashboard.AssignedTask` objects with status ``"done"``.

    **Template:**

    :template:`dashboard/todo_completed.html`
    """
    todo_tasks = AssignedTask.objects.filter(
    child__parent=request.user,
    status="todo"
    ).select_related("child", "task")

    done_tasks = AssignedTask.objects.filter(
        child__parent=request.user,
        status="done"
    ).select_related("child", "task")

    return render(request, "dashboard/todo_completed.html", {
        "todo_tasks": todo_tasks,
        "done_tasks": done_tasks,
        })


def mark_done(request):
    """
    Mark selected assigned chores as completed.

    This view processes a POST request containing selected
    :model:`dashboard.AssignedTask` IDs. It updates each task by:
     - Changing the status from ``"todo"`` to ``"done"``
     - Setting the completion timestamp
     - Awarding one sticker per completed chore

    Only chores belonging to the logged-in parent can be updated.

    **Template:**

    :template:`dashboard/todo_completed.html`
    """
    
    if request.method != "POST":
        return redirect("dashboard:todo_completed")

    check_id = request.POST.getlist("task_ids")  

    # Only update tasks that belong to THIS parent and are still todo
    queryset = AssignedTask.objects.filter(
        id__in=check_id,
        child__parent=request.user,
        status="todo"
    )

    # Mark as done + set completed time + add 1 sticker each
    queryset.update(
        status="done",
        completed_at=timezone.now(),
        stickers_awarded=F("stickers_awarded") + 1
    )
    messages.add_message(
    request, messages.SUCCESS,
    'Keep going you are doing a very good job')
    return redirect("dashboard:todo_completed")
@require_POST
def delete_assigned(request):
    """
    Delete selected assigned chores.
    It is used to remove chores that were assigned by mistake.
    """
    query = request.POST.getlist("task_ids")

    AssignedTask.objects.filter(
        id__in=query,
        child__parent=request.user,
        status="todo",  
    ).delete()
    messages.add_message(
    request, messages.SUCCESS,
    'You have successfully deleted the checked assigned chores.')

    return redirect("dashboard:todo_completed")