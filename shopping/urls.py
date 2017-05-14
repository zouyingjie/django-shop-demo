# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from shopping import views
import shopping.views

app_name = 'shopping'
urlpatterns = [
    url(r'detail/(?P<commodity_id>[0-9]+)', views.CommodityDetailView.as_view(), name='commdity_detail'),
    url(r'list/$', views.CommodityListView.as_view(), name='commdity_list'),
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'register/$', views.RegisterView.as_view(), name='register'),
    url(r'logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'cart/$', views.MyCartView.as_view(), name='my_cart'),
    url(r'addCommodity/$', views.AddToCartView.as_view(), name='add_commodity'),
    url(r'delCommodity/$', views.DeleteFromCartView.as_view(), name='del_commodity'),
    url(r'account/$', views.AccountView.as_view(), name='account'),
    url(r'changeCartitemQuantity/$', views.ChangeCartItemQuantityView.as_view(), name='change_cartitem_quantity'),
    url(r'couponpage/$', views.CouponPageView.as_view(), name='coupon_page'),
    url(r'ordercommitPage/$', views.OrderCommitPageView.as_view(), name='order_commit_page'),
    url(r'ordercancel/$', views.OrderCancelOperationView.as_view(), name='order_cancel'),
    url(r'ordercommit/$', views.OrderCommitOperationView.as_view(), name='order_commit_operation'),
    url(r'takecoupon/$', views.TakeCouponViw.as_view(), name='take_coupon'),
    url(r'ordercommitSuccess/$', views.OrderCommitSuccessView.as_view(), name='order_commit_success'),
]
