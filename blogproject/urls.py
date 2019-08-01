"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings


from blog.feed import  AllPostsRssFeed
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('admin/', xadmin.site.urls),
    path('',include('blog.urls',namespace='blog')),
    url(r'mdeditor/', include('mdeditor.urls')),
    path(r'', include('comments.urls',namespace='comments')),
    #path(r'', include('login.urls',namespace='login')),
    re_path(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
    #搜索功能
    re_path(r'^search/', include('haystack.urls')),
    # django-allauth插件
    re_path(r'^accounts/', include('allauth.urls')),
    # django-allauth用户信息扩展
    re_path(r'^accounts/', include('Myaccount.urls', namespace='accounts')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
