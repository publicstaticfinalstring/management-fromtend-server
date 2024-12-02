import os
import sys
import django

# 添加项目的根目录到Python的路径
sys.path.append('/Users/wuyanze/Devs/Projects/DjangoProject/chances_pear')

# 设置 Django 项目的 settings 模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chances_pear.settings')

# 启动 Django 应用
django.setup()

from apps.contracts.models import Contract

def clear_contract_data():
    # 清除所有合同数据
    deleted_count, _ = Contract.objects.all().delete()
    print(f"已删除 {deleted_count} 条合同数据！")

if __name__ == "__main__":
    clear_contract_data()
