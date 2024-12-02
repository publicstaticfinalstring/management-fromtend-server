
import xadmin
from .models import Task

class TaskAdmin(object):
    list_display = ('name', 'status', 'due_date', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('status', 'due_date')

xadmin.site.register(Task, TaskAdmin)
