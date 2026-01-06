from django.urls import path
from .views import dashboard
from .views import add_child
from .views import edit_child
from .views import delete_child


app_name = "dashboard"
urlpatterns = [ 
    path("", dashboard, name= "dashboard"),
    path("add-child/", add_child, name="add_child"),
    path("edit-child/<int:pk>/", edit_child, name="edit_child"),
    path("delete-child/<int:pk>/", delete_child, name="delete_child"),
]