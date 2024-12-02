
import requests


FEISHU_APP_ID = 'cli_9f6864e72bb6d00e'
FEISHU_APP_SECRET = '6nboFKFZyRwLXEDJzCclyhno8agvuByb'

def get_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = {
        "app_id": FEISHU_APP_ID,
        "app_secret": FEISHU_APP_SECRET
    }
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        token_data = response.json()
        if token_data['code'] == 0:
            return token_data['tenant_access_token']
        else:
            print(f"获取 Access Token 失败，错误码: {token_data['code']}, 错误描述: {token_data['msg']}")
            return None
    else:
        print(f"获取 Access Token 失败，状态码: {response.status_code}, 错误信息: {response.text}")
        return None