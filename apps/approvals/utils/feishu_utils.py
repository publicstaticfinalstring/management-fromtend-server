import requests
from apps.approvals.utils.feishu_auth import get_access_token

class FeishuUtils:
    @staticmethod
    def get_approval_instance_list(access_token, approval_code, start_time, end_time):
        # 获取审批实例列表的函数
        url = "https://open.feishu.cn/open-apis/approval/v4/instances/query"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json; charset=utf-8"
        }
        payload = {
            "approval_code": approval_code,
            "start_time": start_time,
            "end_time": end_time
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        return None

    @classmethod
    def get_or_create_user(cls, access_token, user_id):
        from ..models import User
        try:
            # Try to get the user from the local database
            user = User.objects.get(user_id=user_id)
            return user, False
        except User.DoesNotExist:
            # If the user does not exist, fetch user info from Feishu
            url = f"https://open.feishu.cn/open-apis/contact/v3/users/{user_id}"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json; charset=utf-8"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                user_data = response.json()
                if user_data['code'] == 0:
                    user_info = user_data['data']['user']
                    # Create a new user in the local database
                    user = User.objects.create(
                        user_id=user_info.get('user_id', ''),
                        name=user_info.get('name', '未知'),

                    )
                    return user, True
            return None, False
