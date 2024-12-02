import requests
from .feishu_auth import get_access_token

def get_feishu_multidimensional_sheets(access_token):
    url = "https://open.feishu.cn/open-apis/multidimensional_sheets/v4/list"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"获取飞书多维表格失败，状态码: {response.status_code}, 错误信息: {response.text}")
        return None

def sync_feishu_multidimensional_sheets():
    token = get_access_token()
    if token is None:
        print("获取 Access Token 失败，无法同步多维表格数据")
        return

    multidimensional_sheets = get_feishu_multidimensional_sheets(token)
    if multidimensional_sheets:
        print(f"获取到多维表格数据: {multidimensional_sheets}")
        # 处理多维表格数据

    print("Feishu 多维表格数据同步完成")
