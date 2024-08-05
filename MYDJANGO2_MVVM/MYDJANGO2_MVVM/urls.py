"""
URL configuration for MYDJANGO2_MVVM project.

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
from MYDJANGO2_MVVM import views

urlpatterns = [
    path('', views.index ),
    path('coo', views.coo),
    path('ses_in', views.ses_in, ),
    path('ses_del', views.ses_del),
    path('ses_view', views.ses_view),
    path('coo_in', views.coo_in, ),
    path('coo_del', views.coo_del),
    path('coo_view', views.coo_view),
]
