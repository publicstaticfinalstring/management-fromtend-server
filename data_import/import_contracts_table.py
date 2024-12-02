import csv
import os
import django
import sys

# 设置项目根目录，确保可以正确导入 Django 项目
sys.path.append('/Users/wuyanze/Devs/Projects/DjangoProject/chances_pear')

# 设置 Django 项目环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chances_pear.settings')
django.setup()

from apps.customers.models import Customer
from apps.contracts.models import Contract

def import_contracts_from_csv():
    """
    从同目录下的 contracts_contract.csv 文件导入合同数据到数据库中。
    """
    csv_file_path = os.path.join(os.path.dirname(__file__), 'contracts_contract.csv')
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    customer_id = row['customer_id']
                    customer = Customer.objects.get(customer_id=customer_id)
                    Contract.objects.create(
                        contract_number=row['contract_number'],
                        contract_name=row['contract_name'],
                        customer=customer,
                        contract_amount=row['contract_amount'],
                        signed_date=row['signed_date'],
                        created_at=row['created_at'],
                        updated_at=row['updated_at'],
                        status=row['status'],
                        period=row['period']
                    )
                    print(f"合同 '{row['contract_name']}' 已成功导入。")
                except Customer.DoesNotExist:
                    print(f"客户 ID {customer_id} 不存在，跳过该合同。")
                except Exception as e:
                    print(f"导入合同 '{row['contract_name']}' 时发生错误: {e}")
    except FileNotFoundError:
        print(f"文件 {csv_file_path} 未找到，请检查路径是否正确。")
    except Exception as e:
        print(f"导入过程中发生错误: {e}")

# 示例用法
import_contracts_from_csv()
