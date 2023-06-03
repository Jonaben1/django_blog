from .views import PostList, blog_detail
from django.urls import path


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),
]
