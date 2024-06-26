"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from .views import view, user_detail,product_upload, no_user,helpAdmin

'''id=3 client'''
urlpatterns = [


    path('', user_detail, name='Main'),
    path('client/<int:client_id>/ordered_products/', view, name='index'),
    path('Image_product/image',product_upload, name='Image'),
    path('Message/error',no_user,name='no_user'),
    path('help', helpAdmin, name='help')
]
