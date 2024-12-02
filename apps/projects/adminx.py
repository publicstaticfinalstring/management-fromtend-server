import xadmin
from .models import Project
import xadmin
from .models import Project


class ProjectAdmin:
    # 在列表中显示的字段
    list_display = ['project_name', 'customer', 'total_hours', 'status', 'created_at', 'updated_at']

    # 搜索字段
    search_fields = ['project_name', 'customer__name']

    # 过滤器
    list_filter = ['status', 'created_at', 'updated_at']

    # 自定义排序
    ordering = ['-created_at']

    # 自定义字段显示格式
    def total_hours_display(self, obj):
        return f"{obj.total_hours:.2f} 小时"

    total_hours_display.short_description = '项目总投入工时 (小时)'



try:
    xadmin.site.register(Project, ProjectAdmin)
except xadmin.sites.AlreadyRegistered:
    pass
