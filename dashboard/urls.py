from django.urls import path
from .views import dashboard
from .views import add_child
from .views import edit_child
from .views import delete_child
from .views import assign_tasks
from .views import todo_completed
from .views import mark_done

app_name = "dashboard"
urlpatterns = [ 
    path("", dashboard, name= "dashboard"),
    path("add-child/", add_child, name="add_child"),
    path("edit-child/<int:pk>/", edit_child, name="edit_child"),
    path("delete-child/<int:pk>/", delete_child, name="delete_child"),
    path("assign_tasks/", assign_tasks, name="assign_tasks"),
    path("todo/", todo_completed, name="todo_completed"),
    path("todo/mark-done/", mark_done, name="mark_done"),
]