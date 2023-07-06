from .views import BlogList, blog_detail, CreateBlogPost, ContactView, about
from django.urls import path
from .sitemaps import PostSitemap, StaticSitemap
from django.contrib.sitemaps.views import sitemap



sitemaps = {
    'blog': PostSitemap,
    'static': StaticSitemap,
}

urlpatterns = [
    path('', BlogList.as_view(), name='home'),
    path('<slug:slug>/', blog_detail, name='blog_detail'),
    path('ckeditor/new_post/', CreateBlogPost, name='create'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('contact', ContactView, name='contact'),
    path('about', about, name='about'),
]
