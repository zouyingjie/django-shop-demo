# -*- coding: utf-8 -*-

from django.conf.urls import url
from shopping import views

app_name = 'shopping'

urlpatterns = [
    url(r'detail/(?P<commodity_id>[0-9]+)', views.CommodityDetailView.as_view(), name='commdity_detail'),
    url(r'list/$', views.CommodityListView.as_view(), name='commodity_list'),
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'register/$', views.RegisterView.as_view(), name='register'),
    url(r'logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'cart/$', views.MyCartView.as_view(), name='my_cart'),
    url(r'add_commodity/$', views.AddToCartView.as_view(), name='add_commodity'),
    url(r'del_commodity/$', views.DeleteFromCartView.as_view(), name='del_commodity'),
    url(r'account/$', views.AccountView.as_view(), name='account'),
    url(r'change_cartitem_quantity/$', views.ChangeCartItemQuantityView.as_view(), name='change_cartitem_quantity'),
    url(r'coupon_page/$', views.CouponPageView.as_view(), name='coupon_page'),
    url(r'order_commitPage/$', views.OrderCommitPageView.as_view(), name='order_commit_page'),
    url(r'order_cancel/$', views.OrderCancelOperationView.as_view(), name='order_cancel'),
    url(r'order_commit/$', views.OrderCommitOperationView.as_view(), name='order_commit_operation'),
    url(r'take_coupon/$', views.TakeCouponViw.as_view(), name='take_coupon'),
    url(r'order_commit_success/$', views.OrderCommitSuccessView.as_view(), name='order_commit_success'),
]
