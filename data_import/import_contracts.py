import os
import sys
import django
import pandas as pd

# 添加项目的根目录到Python的路径
sys.path.append('/Users/wuyanze/Devs/Projects/DjangoProject/chances_pear')

# 设置 Django 项目的 settings 模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chances_pear.settings')

# 启动 Django 应用
django.setup()

from apps.contracts.models import Contract
from apps.customers.models import Customer
from django.utils import timezone

def import_contracts():
    file_path = '/Users/wuyanze/Devs/Projects/DjangoProject/chances_pear/data_import/excel/contracts.xlsx'  # 修改为实际的文件路径
    df = pd.read_excel(file_path)

    import_count = 0  # 初始化计数器

    for index, row in df.iterrows():
        try:
            customer = Customer.objects.get(name=row['甲方公司'])

            Contract.objects.create(
                contract_number=row['合同编号'],
                contract_name=row['合同简称'],
                customer=customer,
                contract_amount=row['合同总金额'],
                signed_date=row['签订/生效日期'] if not pd.isna(row['签订/生效日期']) else timezone.now(),
            )

            print(f"合同 {row['合同编号']} 导入成功！")
            import_count += 1  # 每成功导入一条，计数器加1

        except Customer.DoesNotExist:
            print(f"客户 {row['甲方公司']} 不存在，跳过合同 {row['合同编号']}")

    # 输出导入合计
    print(f"合同数据导入完成，共导入 {import_count} 条合同数据！")

if __name__ == "__main__":
    import_contracts()
