
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'api'

urlpatterns = [
    path('auth/token/', obtain_auth_token, name='api_token_auth'),
    
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/<int:user_id>/posts/', views.user_posts, name='user-posts'),
    
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', views.post_comments, name='post-comments'),
    
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    
    path('feed/', views.feed_api, name='feed'),
]