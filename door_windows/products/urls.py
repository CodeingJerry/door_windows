# -*- coding: utf-8 -*-

from django.conf.urls import url
from views import add_products,product_list,uploadavatar,product_detail

urlpatterns = [
    url(r'^add/', add_products, name="add_products"),
    url(r'^list/', product_list, name="product_list"),
    url(r'^detail/(?P<product_id>\d+)', product_detail, name="product_detail"),
    url(r'^uploadavatar/(?P<product_id>\d+)', uploadavatar, name="uploadavatar"),
]