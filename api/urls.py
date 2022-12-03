from django.urls import path
from .views import UserAPIView,UserAPIDetail

urlpatterns = [
    path('users-api/', UserAPIView.as_view(), name='user_api_view'),
    path('user-detail-api/<int:pk>/', UserAPIDetail.as_view(), name='user_detail_api_view'),
]
