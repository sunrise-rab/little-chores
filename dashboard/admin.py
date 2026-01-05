from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Child


# Register your models here.
@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
   list_display = ("name", "parent", "sticker_balance", "created_at")
   list_filter = ("parent",)
   search_fields = ("name",)
