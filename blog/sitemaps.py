from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse




class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'http'


    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.last_modified

    def location(self, obj):
        return f'/{obj.slug}'



class StaticSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return ['home', 'contact', 'about']

    def location(self, item):
        return reverse(item)

