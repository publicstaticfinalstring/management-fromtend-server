
import xadmin
from .models import PresalesProject


class PresalesProjectAdmin:
    # 在列表中显示的字段
    list_display = ['project_name', 'customer', 'project_amount', 'project_status', 'created_at', 'updated_at']

    # 搜索字段
    search_fields = ['project_name', 'customer__name']

    # 过滤器
    list_filter = ['project_status', 'created_at', 'updated_at']

    # 自定义排序
    ordering = ['-created_at']

    # 自定义字段显示格式
    def project_amount_display(self, obj):
        return f"{obj.project_amount:.2f} 元"

    project_amount_display.short_description = '项目金额 (元)'



    model_icon = 'fa fa-user'
    app_label = '管理类'  # 自定义分组名称，显示在菜单栏


    def queryset(self):
        qs = super().queryset()
        # Add additional queries if needed
        return qs


try:
    xadmin.site.register(PresalesProject, PresalesProjectAdmin)
except xadmin.sites.AlreadyRegistered:
    pass
