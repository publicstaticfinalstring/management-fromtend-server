from django.db import models
from django.utils import timezone

class Customer(models.Model):
    # 客户 code
    customer_id = models.IntegerField(verbose_name="客户 ID", unique=True, null=True, blank=True)
    # 客户名称
    name = models.CharField(max_length=255, verbose_name="客户名称", default="未命名客户")
    # 合作开始时间
    cooperation_start_date = models.DateField(verbose_name="合作开始时间", default=timezone.now)
    # 已签订合同数量
    contract_count = models.IntegerField(verbose_name="已签订合同数量", default=0)
    # 累计合同总额
    total_contract_amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="累计合同总额", default=0.00)
    # 售前项目金额
    presales_project_amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="售前项目金额", default=0.00)
    # 已完成待收款金额
    completed_receivable_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="已完成待收款金额", default=0.00)
    # 当前项目投入工时
    current_project_hours = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="当前项目投入工时", default=0.00)
    # 当前项目数量
    current_project_count = models.IntegerField(verbose_name="当前项目数量", default=0)
    # 创建时间
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    # 更新时间
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    # 状态
    status = models.CharField(verbose_name="状态", max_length=20, default="active")
    # 省份
    province = models.CharField(max_length=100, verbose_name="省份", default="未知")
    # 级别
    level = models.CharField(max_length=50, verbose_name="级别", default="普通")

    class Meta:
        verbose_name = "客户"
        verbose_name_plural = "客户管理"

    def __str__(self):
        return self.name
