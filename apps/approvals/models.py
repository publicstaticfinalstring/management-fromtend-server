from django.db import models

class Approval(models.Model):
    approval_code = models.CharField(max_length=255, verbose_name='审批编号', default='')
    approval_name = models.CharField(max_length=255, verbose_name='审批名称', default='')
    applicant = models.CharField(max_length=255, verbose_name='申请人', default='')
    status = models.CharField(
        max_length=50,
        choices=[
            ('PENDING', '审批中'),
            ('RECALL', '撤回'),
            ('REJECT', '拒绝'),
            ('DELETED', '已删除'),
            ('APPROVED', '通过')
        ],
        verbose_name='审批状态',
        default='PENDING'
    )
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    instance_code = models.CharField(max_length=255, verbose_name='实例代码', default='')
    end_time = models.DateTimeField(verbose_name='结束时间', null=True, blank=True)
    external_id = models.CharField(max_length=255, verbose_name='外部 ID', default='', blank=True)
    extra = models.TextField(verbose_name='额外信息', default='', blank=True)
    serial_id = models.CharField(max_length=255, verbose_name='序列号', default='', blank=True)
    title = models.CharField(max_length=255, verbose_name='标题', default='', blank=True)

    class Meta:
        verbose_name = '审批流程'
        verbose_name_plural = '审批流程管理'
from django.db import models

# User model for storing user information from Feishu
class User(models.Model):
    user_id = models.CharField(max_length=255, unique=True, verbose_name='用户ID')
    name = models.CharField(max_length=255, verbose_name='姓名', default='未知')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户管理'

    def __str__(self):
        return self.name if self.name else self.user_id

# Type model for storing different types of approval or categories
class Type(models.Model):
    type_code = models.CharField(max_length=255, unique=True, verbose_name='类型编码')
    type_name = models.CharField(max_length=255, verbose_name='类型名称')

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = '类型管理'

    def __str__(self):
        return self.type_name