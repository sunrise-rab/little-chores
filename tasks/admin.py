from atexit import register
from django.contrib import admin
from .models import Task
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):

    list_display = ('title','description','benefits', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    summernote_fields = ('description','benefits', )


