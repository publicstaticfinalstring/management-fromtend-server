import requests
from .feishu_auth import get_access_token

def get_feishu_documents(access_token):
    url = "https://open.feishu.cn/open-apis/docs/v4/list"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"获取飞书文档失败，状态码: {response.status_code}, 错误信息: {response.text}")
        return None

def sync_feishu_documents():
    token = get_access_token()
    if token is None:
        print("获取 Access Token 失败，无法同步文档数据")
        return

    documents = get_feishu_documents(token)
    if documents:
        print(f"获取到文档数据: {documents}")
        # 处理文档数据

    print("Feishu 文档数据同步完成")
