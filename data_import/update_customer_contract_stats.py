import os
import sys
import django


# 添加项目根目录到 Python 路径
sys.path.append('/Users/wuyanze/Devs/Projects/DjangoProject/chances_pear')

# 设置 Django 项目的 settings 模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chances_pear.settings')

# 启动 Django 应用
django.setup()

from apps.contracts.models import Contract
from apps.customers.models import Customer

from django.db.models import Count, Sum

from decimal import Decimal, InvalidOperation

def convert_to_decimal(value, default=Decimal('0.00')):
    """
    尝试将传入的值转换为 Decimal，如果失败则返回默认值。
    """
    try:
        if value is None or value == '':
            return default
        return Decimal(str(value))
    except InvalidOperation:
        # 捕获 Decimal 转换失败，返回默认值
        return default

def update_customer_contract_stats(customer_id=None):
    customers = Customer.objects.all() if customer_id is None else Customer.objects.filter(id=customer_id)

    for customer in customers:
        # 统计每个客户的合同数量和合同总额
        contract_stats = Contract.objects.filter(customer=customer).aggregate(
            contract_count=Count('id'),
            total_contract_amount=Sum('contract_amount')
        )

        # 输出调试信息
        print(f"Processing customer: {customer.name}")
        print(f"Contract stats: {contract_stats}")

        # 转换合同总额
        total_amount = convert_to_decimal(contract_stats['total_contract_amount'])
        print(f"Total amount before save: {total_amount}")  # 调试输出合同金额

        # 更新客户的合同总额和合同数量
        customer.total_contract_amount = total_amount
        customer.contract_count = contract_stats['contract_count'] or 0

        # 保存客户数据前，检查 DecimalField
        try:
            customer.save()
            print(f"Customer {customer.name} saved successfully with total_contract_amount={customer.total_contract_amount}")
        except InvalidOperation:
            print(f"Error saving customer {customer.name}: Invalid decimal value, total_contract_amount={total_amount}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    print("客户合同统计信息更新完成！")


if __name__ == "__main__":
    update_customer_contract_stats()


