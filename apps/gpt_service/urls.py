from django.urls import path
from . import views

urlpatterns = [
    path('analyze_data/', views.analyze_data_view, name='analyze_data'),
]
