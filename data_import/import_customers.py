import os
import sys
import django
import pandas as pd
from django.core.wsgi import get_wsgi_application
import datetime

# 添加项目的根目录到Python的路径
sys.path.append('/Users/wuyanze/Devs/Projects/DjangoProject/chances_pear')

# 设置 Django 项目的 settings 模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chances_pear.settings')

# 启动 Django 应用
application = get_wsgi_application()
django.setup()

from apps.customers.models import Customer  # 在设置好 Django 环境后再导入模型


# 定义数据导入函数
def import_customers():
    # 清空所有现有的客户数据
    Customer.objects.all().delete()
    print("已清除所有现有的客户数据")

    file_path = '/Users/wuyanze/Devs/Projects/DjangoProject/chances_pear/data_import/excel/customer.xlsx'  # 修改为实际的文件路径
    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        cooperation_start_year = row['开始合作时间']

        # 如果年份是整数或者字符串，转换为日期格式：年份-01-01
        if isinstance(cooperation_start_year, (int, str)):
            try:
                # 将年份转换为日期对象，默认设置为该年的1月1日
                cooperation_start_date = datetime.date(int(cooperation_start_year), 1, 1)
            except ValueError:
                cooperation_start_date = None  # 如果解析失败，设置为 None 或者其他默认值
        else:
            cooperation_start_date = None  # 如果不是整数或字符串，设置为 None

        # 创建 Customer 实例
        Customer.objects.create(
            name=row['客户名称'],
            province=row['省份'],
            level=row['级别'],
            cooperation_start_date=cooperation_start_date,
        )

    print("Customer data imported successfully!")


if __name__ == "__main__":
    import_customers()
