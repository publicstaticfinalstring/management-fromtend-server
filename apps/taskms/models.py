from django.db import models
from apps.projects.models import Project

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending_schedule', '待排期'),
        ('scheduled', '已排期'),
        ('in_development', '研发中'),
        ('pending_testing', '待测试'),
        ('in_testing', '测试中'),
        ('pending_package', '待出包'),
        ('pending_upgrade', '待升级'),
        ('completed', '完成'),
        ('paused', '暂停'),
        ('cancelled', '取消'),
    ]
    name = models.CharField(verbose_name='任务名称', max_length=100, unique=True, default='默认任务名称')  # 任务名称
    title = models.CharField(verbose_name='任务标题', max_length=255, default='默认任务标题')  # 为 title 字段添加默认值
    description = models.TextField("任务描述", blank=True, null=True)
    project = models.ForeignKey(Project,verbose_name='所属项目', on_delete=models.CASCADE, default=1)  # 假设 ID 为 1 的项目是默认项目
    status = models.CharField(verbose_name='任务状态',max_length=20, choices=STATUS_CHOICES, default='pending_schedule')  # 设置默认值
    assigned_to = models.CharField("负责人", max_length=255, blank=True, null=True)
    due_date = models.DateField("截止日期", blank=True, null=True)
    completed = models.BooleanField("是否完成", default=False)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "任务"
        verbose_name_plural = "任务管理"
