from django.shortcuts import render
from django.views import generic
from .models import Task

# Create your views here.
class TaskList(generic.ListView):
    queryset = Task.objects.all().filter(status=1).order_by("age_group")
    template_name = "tasks/index.html"
    context_object_name = "task_list"


    

