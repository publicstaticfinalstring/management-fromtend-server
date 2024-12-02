import requests
from .feishu_auth import get_access_token
from apps.approvals.models import Approval

def get_approval_instance_list(access_token, approval_code):
    url = "https://open.feishu.cn/open-apis/approval/v4/instances/:instance_id"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    payload = {
        "approval_code": approval_code,  # 添加必须的 approval_code
        "form": {},  # 需要根据实际需求构造 form 字段
        "page_size": 10  # 根据需要设置分页大小
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"获取审批实例失败，状态码: {response.status_code}, 错误信息: {response.text}")
        return None

def sync_feishu_approvals():
    token = get_access_token()  # 每次调用 API 前都获取最新的 token
    if token is None:
        print("获取 Access Token 失败，无法同步审批数据")
        return

    # 假设我们有一些审批代码
    approval_codes = ['approval_code_1', 'approval_code_2']
    for approval_code in approval_codes:
        instances = get_approval_instance_list(token, approval_code)
        if instances:
            print(f"获取到审批实例: {instances}")
            for instance in instances.get('data', {}).get('items', [])[:5]:
                instance_code = instance.get('instance_code')
                approval_name = instance.get('approval_code')

                # 创建或更新审批流程记录
                approval, created = Approval.objects.update_or_create(
                    instance_code=instance_code,
                    defaults={
                        'approval_name': approval_name,
                        # 根据实际数据结构保存更多字段
                    }
                )

                if created:
                    print(f"新增审批流程: {approval_name}")
                else:
                    print(f"更新审批流程: {approval_name}")

    print("Feishu 审批流程数据同步完成")
