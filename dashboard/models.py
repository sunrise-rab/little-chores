from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from tasks.models import Task


# Create your models here.

User = get_user_model()

class Child(models.Model):
   parent = models.ForeignKey(
       User,
       on_delete=models.CASCADE,
       related_name="children"
   )
   name = models.CharField(max_length=100)
   date_of_birth = models.DateField(null=True, blank=True)
   sticker_balance = models.PositiveIntegerField(default=0)
   created_at = models.DateTimeField(auto_now_add=True)

   class Meta:
       ordering = ["name"]

   def __str__(self):
       return f"{self.name}"
    
   def age(self):
       """
       Return the child's age in years.
       """
       today = date.today()
       return today.year - self.date_of_birth.year - ((today.month,today.day)<(self.date_of_birth.month, self.date_of_birth.day))
       
   def age_group(self):
        """
        Return age_group based on age.
        """
        age= self.age()
        if age <= 5 :
            return 1
        elif age <= 8:
            return 2
        elif age <= 11:
            return 3
        return 4

class AssignedTask(models.Model):
     STATUS_CHOICES = (
        ("todo", "To do"),
        ("done", "Completed"),
    )
     child = models.ForeignKey(Child,on_delete=models.CASCADE, related_name="assigned_tasks")
     task = models.ForeignKey(Task, on_delete=models.CASCADE,related_name="assigned_tasks")
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
     assigned_at = models.DateTimeField(auto_now_add=True)
     completed_at = models.DateTimeField(null=True, blank=True)
     stickers_awarded = models.PositiveIntegerField(default=0)

     class Meta:
         ordering = ["status", "-assigned_at"]

     def __str__(self):
         return f"{self.task.title}  {self.child.name}"




