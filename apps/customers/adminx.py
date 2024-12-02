import xadmin
from .models import Customer

class CustomerAdmin:
    # 显示在列表中的字段
    list_display = ['name', 'cooperation_start_date', 'contract_count',
                    'total_contract_amount', 'presales_project_amount',
                    'completed_receivable_amount', 'current_project_hours',
                    'current_project_count', 'status', 'province', 'level',
                    'created_at', 'updated_at']

    # 搜索字段
    search_fields = ['name', 'province', 'level']

    # 列表过滤器
    list_filter = ['cooperation_start_date', 'created_at', 'updated_at', 'province', 'level', 'status']

    # 自定义排序
    ordering = ['-created_at']

    # 确保数值字段显示正确的千分位和小数点格式
    def total_contract_amount(self, obj):
        return f"{obj.total_contract_amount:,.2f}"

    total_contract_amount.short_description = '累计合同总额 (元)'

    def presales_project_amount(self, obj):
        return f"{obj.presales_project_amount:,.2f}"

    presales_project_amount.short_description = '售前项目金额 (元)'

    def completed_receivable_amount(self, obj):
        return f"{obj.completed_receivable_amount:,.2f}"

    completed_receivable_amount.short_description = '已完成待收款金额 (元)'

# 注册管理类
xadmin.site.register(Customer, CustomerAdmin)
