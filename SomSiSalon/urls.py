"""SomSiSalon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from functools import cached_property
from django.contrib import admin
from django.urls import path

from index import views as index_views
from aboutus import views as aboutus_views
from service import views as service_views
from product import views as product_views
from appointment import views as appointment_views
from cart import views as cart_views
from cusprofile import views as cusprofile_views
from checkout import views as checkout_views


urlpatterns = [

    # admin path
    path('admin/', admin.site.urls),

    # index path
    path('', index_views.index, name='index'),
    path('index', index_views.index, name='index'),


    # other page index
    path('aboutus', aboutus_views.index, name='about_us'),
    path('service', service_views.index, name='service'),
    path('product', product_views.index, name='product'),
    path('appointment', appointment_views.index, name='appointment'),
    path('cart', cart_views.index, name='cart'),
    path('profile', cusprofile_views.index, name='cusprofile'),
    path('checkout/delivery_detail', checkout_views.index, name='checkout'),

    # index
    path('best_product_seller', index_views.BestProductSeller.as_view(),
         name='BestProductSeller'),
    path('best_service_seller', index_views.BestServiceSeller.as_view(),
         name='BestServiceSeller'),

    path('mail_register_for_infomation', index_views.MailRegister.as_view(),
         name='MailRegisterForInfomation'),

    #
]
