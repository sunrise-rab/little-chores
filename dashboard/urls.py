from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [ 
    path("", views.dashboard, name= "dashboard"),
    path("add-child/", views.add_child, name="add_child"),
    path("edit-child/<int:pk>/", views.edit_child, name="edit_child"),
    path("delete-child/<int:pk>/", views.delete_child, name="delete_child"),
    path("assign_tasks/", views.assign_tasks, name="assign_tasks"),
    path("todo/", views.todo_completed, name="todo_completed"),
    path("todo/mark-done/", views.mark_done, name="mark_done"),
    path("todo/delete/", views.delete_assigned, name="delete_assigned"),
]