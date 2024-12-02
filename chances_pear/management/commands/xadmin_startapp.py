from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Create a new Django app with xadmin setup'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='Name of the new application')

    def handle(self, *args, **options):
        app_name = options['app_name']
        # 使用 Django 标准命令创建应用
        os.system(f'python manage.py startapp {app_name}')

        # 创建 xadmin 配置文件
        admin_file_content = """
import xadmin
from .models import Task

class TaskAdmin(object):
    list_display = ('name', 'status', 'due_date', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('status', 'due_date')

xadmin.site.register(Task, TaskAdmin)
"""

        admin_file_path = os.path.join(app_name, 'admin.py')
        with open(admin_file_path, 'w') as file:
            file.write(admin_file_content)

        self.stdout.write(self.style.SUCCESS(f'Successfully created and configured the {app_name} application with xadmin.'))
