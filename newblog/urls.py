"""
URL configuration for newblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .view1 import start_pr, start_one, salom, qadam, qadam5, qadam6, qadam7, qadam8, qadam9, qadamend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Start1/', salom),
    path('Start2/', start_pr),
    path('Start3/', start_one),
    path('Start4/', qadam),
    path('Start5/', qadam5),
    path('Start6/', qadam6),
    path('Start7/', qadam7),
    path('Start8/', qadam8),
    path('Start9/', qadam9),
    path('End10/',qadamend)
]
