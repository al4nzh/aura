from django.urls import path
from .views import UserPostsView, OtherUserPostsView

urlpatterns = [
    path('my_posts/', UserPostsView.as_view(), name = 'my_posts'),
    path('user-posts/<str:username>/', OtherUserPostsView.as_view(), name='user-posts'),
]