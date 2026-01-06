from django.db import models
from django.contrib.auth import get_user_model


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


