from django.shortcuts import render,redirect, get_object_or_404
from .models import Child
from .forms import ChildForm

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


     
   

