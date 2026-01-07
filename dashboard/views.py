from tokenize import group
from django.shortcuts import render,redirect, get_object_or_404

from tasks.models import AGE_GROUP_CHOICES
from .models import Child
from .forms import ChildForm
from tasks.models import Task
from .forms import AssignChoresForm
from .models import AssignedTask

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