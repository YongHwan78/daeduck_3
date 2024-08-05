"""
URL configuration for MYDJANGO_MEM project.

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
from MYDJANGO_MEM import views

urlpatterns = [
    path('', views.main),
    path('mem_list', views.mem_list),
    path('mem_detail', views.mem_detail),
    path('mem_mod', views.mem_mod),
    path('mem_mod_act', views.mem_mod_act),
    path('mem_add', views.mem_add ),
    path('mem_add_act', views.mem_add_act  ),
    path('mem_delete_act' , views.mem_delete_act ),
]
