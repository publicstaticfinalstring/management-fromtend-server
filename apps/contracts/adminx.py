import xadmin
from django.utils.html import format_html

from .models import Contract


class ContractAdmin(object):
    list_display = ['contract_number', 'customer', 'signed_date', 'status']
    search_fields = ['contract_number', 'customer__name']
    list_filter = ['status', 'signed_date']

    # 自定义在列表中显示图片预览
    def attachment_image_tag(self, obj):
        if obj.attachment_image:
            return format_html('<img src="{}" width="100" height="100" />', obj.attachment_image.url)
        return '-'

    attachment_image_tag.short_description = '合同附件预览'

    model_icon = 'fa fa-user'
    app_label = '管理类'  # 自定义分组名称，显示在菜单栏


    def queryset(self):
        qs = super().queryset()
        # Add additional queries if needed
        return qs


try:
    xadmin.site.register(Contract, ContractAdmin)
except xadmin.sites.AlreadyRegistered:
    pass
