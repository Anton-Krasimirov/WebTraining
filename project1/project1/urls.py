"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

from project1.employees.views import home, not_found, go_to_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'), # 127.0.0.1:8000/department/    and 127.0.0.1:8000
    path('department/', include('project1.employees.urls')), # 127.0.0.1:8000/department/1/ 2,3,4 /department/
    path('go_to_home/', go_to_home, name='go to home'),
    path('not_found/', not_found),
]