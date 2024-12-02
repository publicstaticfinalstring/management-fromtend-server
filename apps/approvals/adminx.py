import xadmin
from .models import Approval

class ApprovalAdmin(object):
    list_display = [
        'instance_code',
        'approval_name',
        'applicant',
        'status',
        'create_time',
        'end_time',
        'external_id',
        'serial_id',
        'title'
    ]
    model_icon = 'fa fa-check-square-o'

xadmin.site.register(Approval, ApprovalAdmin)
