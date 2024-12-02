from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth import get_user_model

from django.db import models


# Create your models here.


class UserProfile(models.Model):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female",
                              verbose_name="性别")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    REQUIRED_FIELDS = ['email', 'mobile']

    class Meta:
        app_label = 'users'
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code



