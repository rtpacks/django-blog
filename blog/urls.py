"""blog URL Configuration

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
from django.conf.urls.static import static
from . import views
from django.urls import path, include
import extra_apps.xadmin as xadmin

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('admin/', xadmin.site.urls,name='adminx'),
    path('feedback/', views.feedback, name='feedback'),

    path('user/',include('apps.user.urls')),

    path('',include('apps.article.urls')),
    path('article/',include('apps.article.urls')),
]


# 开发模式下，默认配置
from blog import settings
from blog.settings import MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)