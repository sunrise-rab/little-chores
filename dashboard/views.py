from tokenize import group
from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from tasks.models import AGE_GROUP_CHOICES
from .models import Child
from .forms import ChildForm
from tasks.models import Task
from .forms import AssignChoresForm
from .models import AssignedTask
from django.db.models import F 

# Create your views here.
def dashboard(request):
    children = Child.objects.filter(parent=request.user)
  
    return render(
        request, 
        "dashboard/dashboard.html", 
        {
        "children": children,
     
        
        })

def add_child(request):
    if request.method == "POST":
        child_form = ChildForm(request.POST)
        if child_form.is_valid():
            child = child_form.save(commit=False)
            child.parent = request.user
            child.save()
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
                AssignedTask.objects.get_or_create(child=child, task=task)

            return redirect("dashboard:dashboard")

    return render(request, "dashboard/assign_tasks.html", {"form": form})
   
def todo_completed(request):
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

    return redirect("dashboard:todo_completed")