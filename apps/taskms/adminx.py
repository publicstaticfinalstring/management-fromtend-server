import xadmin
from .models import Task

class TaskAdmin(object):
    # 定义后台显示的字段
    list_display = ('title', 'status', 'due_date', 'assigned_to_display', 'project_display', 'created_at', 'updated_at')

    # 定义可以通过哪些字段进行搜索
    search_fields = ('title', 'description', 'project__title')  # 搜索 'title'、'description' 和 'project' 的 'title' 字段

    # 定义筛选器，便于在后台进行筛选
    list_filter = ('status', 'due_date', 'assigned_to', 'project')  # 按照 'status'、'due_date' 等字段过滤

    # 定义图标
    model_icon = 'fa fa-tasks'
    app_label = "内部管理"  # 设置应用分组显示


    def get_queryset(self, request):
        queryset = super(TaskAdmin, self).get_queryset(request)
        return queryset.select_related('project', 'assigned_to')  # 预取关联的字段

    def assigned_to_display(self, obj):
        return obj.assigned_to.username if obj.assigned_to else '未分配'

    assigned_to_display.short_description = '负责人'

    def project_display(self, obj):
        return obj.project.title if obj.project else '未关联项目'

    project_display.short_description = '项目'

try:
    xadmin.site.register(Task, TaskAdmin)
except xadmin.sites.AlreadyRegistered:
    pass  # 如果 Task 已经注册，忽略这个异常
