from django.urls import path
from .views import dashboard
from .views import add_child


app_name = "dashboard"
urlpatterns = [ 
    path("", dashboard, name= "dashboard"),
    path("add-child/", add_child, name="add_child"),
]