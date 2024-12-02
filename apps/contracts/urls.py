from django.urls import path
from .views import upload_contract_image  # 确保导入了正确的视图

urlpatterns = [
    path('upload/', upload_contract_image, name='upload_contract_image'),
]
