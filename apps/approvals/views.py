from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Approval
from apps.approvals.utils.feishu_utils import FeishuUtils
from apps.approvals.utils.feishu_utils  import get_access_token
import datetime

import json

# View to handle fetching approval orders
class ApprovalListView(View):
    def get(self, request):
        # Get access token
        # Get access token
        access_token = get_access_token()
        if not access_token:
            return JsonResponse({'error': 'Failed to get access token from Feishu'}, status=500)

        # Set start and end times (in seconds since epoch)
        start_time = int(datetime.datetime.strptime("20220101000000", "%Y%m%d%H%M%S").timestamp())
        end_time = int(datetime.datetime.now().timestamp())
        # Initialize an empty list to collect all approvals
        all_approvals = []
        # Get approval instances list
        approval_codes = [
            '857CF56E-DBC2-428D-A0D0-9518B4F4DA89',

        ]
        for approval_code in approval_codes:
            approval_instances = FeishuUtils.get_approval_instance_list(access_token, approval_code, start_time,
                                                                        end_time)
            if approval_instances:
                approvals = approval_instances.get('data', {}).get('instance_list', [])
                for approval in approvals:
                    user_id = approval['instance'].get('user_id')
                    if user_id:
                        # First, try to get user info from the local database or Feishu
                        user, created = FeishuUtils.get_or_create_user(access_token, user_id)
                        if user is not None:
                            approval['instance']['user_name'] = user.name
                        else:
                            # Assign a default value or skip if user not found
                            approval['instance']['user_name'] = '未知用户'
                    # Save or update approval data in the database
                    # Save or create approval data in the database
                    Approval.objects.create(
                        approval_code=str(approval['approval'].get('approval_id', '')).replace(',', ''),
                        approval_name=approval['approval'].get('name', ''),
                        applicant=approval['instance'].get('user_name', '未知用户'),
                        status=approval['instance'].get('status', '').upper(),
                        create_time=datetime.datetime.fromtimestamp(
                            int(approval['instance'].get('start_time', 0)) / 1000),
                        instance_code=approval['instance'].get('code', ''),
                        end_time=datetime.datetime.fromtimestamp(int(approval['instance'].get('end_time', 0)) / 1000) if
                        approval['instance'].get('end_time') != '0' else None,
                        external_id=approval['instance'].get('external_id', ''),
                        extra=approval['instance'].get('extra', ''),
                        serial_id=approval['instance'].get('serial_id', ''),
                        title=approval['instance'].get('title', '')
                    )

                all_approvals.extend(approvals)
            else:
                return JsonResponse({'error': f'Failed to fetch approvals for code {approval_code}'}, status=500)

        return JsonResponse({'approvals': all_approvals}, safe=False,
                            json_dumps_params={'indent': 4, 'ensure_ascii': False})

