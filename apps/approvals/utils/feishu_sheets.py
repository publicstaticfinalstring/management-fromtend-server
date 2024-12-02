import requests
from .feishu_auth import get_access_token

def get_feishu_sheets(access_token):
    url = "https://open.feishu.cn/open-apis/sheets/v4/list"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"获取飞书表格失败，状态码: {response.status_code}, 错误信息: {response.text}")
        return None

def sync_feishu_sheets():
    token = get_access_token()
    if token is None:
        print("获取 Access Token 失败，无法同步表格数据")
        return

    sheets = get_feishu_sheets(token)
    if sheets:
        print(f"获取到表格数据: {sheets}")
        # 处理表格数据

    print("Feishu 表格数据同步完成")
