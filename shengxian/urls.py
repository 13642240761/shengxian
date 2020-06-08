"""shengxian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import RedirectView

import xadmin
from apps.goods.views import IndexView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),  # 使用xadmin
    #path('', IndexView.as_view(), name='index'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('search/', include('haystack.urls')),  # 全文检索框架
    path('user/', include('apps.user.urls', namespace='user')),  # 用户模块
    path('cart/', include('apps.cart.urls', namespace='cart')),  # 购物车模块
    path('order/', include('apps.order.urls', namespace='order')),  # 订单模块
    path('', include('apps.goods.urls', namespace='goods')),  # 商品模块
    # favicon.ico
    path("favicon.ico", RedirectView.as_view(url='static/images/favicon.ico')),

]
