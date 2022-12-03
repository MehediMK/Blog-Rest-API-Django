from django.urls import path
from .views import (PostApiList, PostApiDetail, AddPostApiView, CommentList, CommentDetail, CategoryList, CategoryDetail)

urlpatterns = [
    path('post-api/view/', PostApiList.as_view(), name='post_api_view'),
    path('post-api/add/', AddPostApiView.as_view(), name='add_post_api'),
    path('post-api/<int:pk>/', PostApiDetail.as_view(), name='post_detail_api'),
    path('post-api/comments/', CommentList.as_view(), name='comment'),
    path('post-api/comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path('categories/', CategoryList.as_view(), name='categories_api'),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
]
