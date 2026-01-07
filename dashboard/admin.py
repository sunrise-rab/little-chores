from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Child
from .models import AssignedTask


# Register your models here.
@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
   list_display = ("name", "parent", "sticker_balance", "created_at")
   list_filter = ("parent",)
   search_fields = ("name",)

@admin.register(AssignedTask)
class AssignedTaskAdmin(admin.ModelAdmin):
   list_display = ("child", "task", "status", "assigned_at", "completed_at","stickers_awarded" )
   list_filter = ("status",)
   search_fields = ("assigned_at",)
