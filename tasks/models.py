from django.db import models
from django.contrib.auth.models import User # Import models to connect

# Create your models here.

STATUS = ((0, "Unapproved"), (1, "Approved"))
class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name="blog_posts"
        )
    description = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
