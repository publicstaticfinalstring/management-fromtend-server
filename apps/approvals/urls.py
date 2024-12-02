# customers/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApprovalListView


# 将路由器的 URLs 列表包含进来
urlpatterns = [
    path('approvals/', ApprovalListView.as_view(), name='feishu_approvals'),
]
