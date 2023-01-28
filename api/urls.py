from django.urls import path
from .views import UserAPIView,UserAPIDetail,UserAPIDetail,UserCreateAPIView,UserDestroyAPIView

urlpatterns = [
    path('users-api/', UserAPIView.as_view(), name='user_api_view'),
    path('user-detail-api/<int:pk>/', UserAPIDetail.as_view(), name='user_detail_api_view'),
    path('user_delete_api_view/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete_api_view'),
    path('user_create_api/', UserCreateAPIView.as_view(), name='user_create_api'),
]
