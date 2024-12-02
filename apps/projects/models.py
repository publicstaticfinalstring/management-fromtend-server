from django.db import models
from apps.customers.models import Customer
from django.utils import timezone

class Project(models.Model):
    # 项目名称
    project_name = models.CharField(max_length=255, verbose_name="项目名称", default="未命名项目")
    # 客户
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="客户")
    # 项目总投入工时
    total_hours = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="项目总投入工时", default=0.00)
    # 项目状态
    status = models.CharField(max_length=50, verbose_name="项目状态", default="进行中")
    # 创建时间
    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    # 更新时间
    updated_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目管理"

    def __str__(self):
        return self.project_name
