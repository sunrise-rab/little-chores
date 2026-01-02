from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

AGE_GROUP_CHOICES = [
    (1, "Ages 3–5"),
    (2, "Ages 6–8"),
    (3, "Ages 9–11"),
    (4, "Ages 12+"),
]

STATUS = ((0, "Unapproved"), (1, "Approved"))
class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name="admin_tasks"
        )
    age_group = models.PositiveSmallIntegerField(
        choices=AGE_GROUP_CHOICES
        )
    description = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"The title of this post is {self.title}"
