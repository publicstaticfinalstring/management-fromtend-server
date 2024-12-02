from django.db import models
from apps.customers.models import Customer
from django.utils import timezone

class MyModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

class PresalesProject(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="客户")
    project_name = models.CharField(max_length=100, verbose_name="项目名称")
    project_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="项目金额")
    project_status = models.CharField(max_length=50, choices=[('ongoing', '进行中'), ('completed', '已完成')], verbose_name="项目状态")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "售前项目"
        verbose_name_plural = "售前项目管理"

    def __str__(self):
        return self.project_name
