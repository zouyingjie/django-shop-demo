# -*- coding: utf-8 -*-
import random
import datetime

from decimal import Decimal
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.utils import timezone

from pure_pagination import Paginator, PageNotAnInteger

from shopping import models

PER_PAGE_NUM = 18


# TODO: 用户相关服务
def login_service(request, user):
    """
    用户登录服务
    :param request:
    :param user:
    :return:
    """
    login(request, user)


def register_service(request):
    """
    用户注册服务
    :return:
    """

    user_phone = request.POST.get("phone")
    user_email = request.POST.get("email")
    user_name = request.POST.get("name")
    user_pwd = request.POST.get("password")

    user = models.User()
    user.username = user_name
    user.user_email = user_email
    user.user_phone = user_phone
    user.password = make_password(user_pwd)
    user.save()


def logout_service(request):
    """
    退出登录服务
    :param request:
    :return:
    """
    logout(request)


# TODO : 购物车的相关服务


def check_cart_record_service(user_id):
    """
    查看购物车商品服务
    :return:
    """
    cart_items = models.Cart.objects.filter(user_id=user_id)

    return cart_items


def add_to_cart_service(commodity_id, user_id):
    """
    添加商品到购物车
    """

    commodity = models.Commodity.objects.get(pk=commodity_id)

    cart_items = models.Cart.objects.filter(commodity_id=commodity_id, user_id=user_id)
    if len(cart_items) == 0:
        new_cart_item = models.Cart()
        new_cart_item.commodity_id = commodity_id
        new_cart_item.user_id = user_id
        new_cart_item.quantity = 1
        new_cart_item.price = commodity.price
        new_cart_item.total_price = commodity.price
        new_cart_item.title = commodity.title
        new_cart_item.pic1 = commodity.pic1
        new_cart_item.save()
    else:
        old_item = cart_items[0]
        old_item.quantity = old_item.quantity + 1
        old_item.total_price = old_item.total_price + commodity.price
        old_item.save()


def cart_account_service(cart_item_ids):
    """
    购物车结算服务
    :param cart_item_ids:
    :return:
    """
    for cart_item_id in cart_item_ids:
        cart_item = models.Cart.objects.get(pk=cart_item_id)
        cart_item.has_check = 1  # 代表被选中进行结算
        cart_item.save()


def change_cart_quantity_service(user_id, commodity_id, quantity):
    """
    修改购物车中商品的数量
    :param cart_item_ids:
    :return:
    """
    cart_item = models.Cart.objects.filter(user_id=user_id, commodity_id=commodity_id).first()
    cart_item.quantity = quantity
    cart_item.total_price = cart_item.price * Decimal(cart_item.quantity)
    cart_item.save()
    return cart_item


def delete_cart_commodity_service(user_id, commodity_id):
    """
    从购物车删除服务
    :return:
    """
    cart_item = models.Cart.objects.filter(commodity_id=commodity_id, user_id=user_id)[0]
    cart_item.delete()


def commit_order_page_service(user_id):
    """
    访问订单提交界面的服务
    :param user_id:
    :return: 返回提交的商品项和可用的优惠券
    """
    # cart = models.Cart.objects.get(user_id=user_id)
    commit_cart_items = models.Cart.objects.filter(user_id=user_id, has_check=1)

    # 获取用户优惠券对应关系数据
    user_to_coupons = list(models.UserToCoupon.objects.filter(user_id=user_id))

    # 获取未过期的优惠券
    unexpire_user_tp_coupons = [x for x in user_to_coupons if x.end_time > timezone.now()]

    # 根据未过期未使用的用户券关系获取到所有的优惠券
    coupons = list()
    if len(unexpire_user_tp_coupons) > 0:
        for unexpire_user_tp_coupon in unexpire_user_tp_coupons:
            coupon = models.Coupon.objects.filter(coupon_id=unexpire_user_tp_coupon.coupon_id,
                                                  statue=2).first()
            if coupon is not None:
                coupons.append(coupon)
    return commit_cart_items, coupons


@transaction.atomic
def generate_order_service(user_id, coupon_id, total_price, discount_price):
    """
    购物车生成订单服务
    :return:
    """

    '''
    1.修改用到的优惠券状态
    2.获取到所有要结算的购物车项
    3.生成订单信息与订单商品信息
    4.将购物车项信息删除
    '''
    if coupon_id != '*' and coupon_id != 'undefined':
        coupon = models.Coupon.objects.get(pk=coupon_id)
        coupon.statue = 3
        coupon.save()

    all_cart_items = models.Cart.objects.filter(user_id=user_id, has_check=1)
    order = models.Order()
    order.order_id = int(random.uniform(1, 100) * 10000000000)
    order.user_id = user_id
    order.total_price = total_price
    order.discount_price = discount_price
    # TODO:待添加的收货人信息、物流信息、支付信息以及订单状态

    order.receiver_info_id = "111111111"
    order.distribution_info_id = '2222222222'
    order.pay_info_id = '3333333333'
    order.statue = 1
    order.save()

    for items in all_cart_items:
        order_commodity_item = models.OrderCommodityItem()
        order_commodity_item.id = int(random.uniform(1, 100) * 10000000000)
        order_commodity_item.order_id = order.order_id
        order_commodity_item.price = items.price
        order_commodity_item.quantity = items.quantity
        order_commodity_item.commodity_id = items.commodity_id
        order_commodity_item.save()

    all_cart_items.delete()


def cancel_order_service(user_id):
    """
    订单取消服务
    :return:
    """
    commit_cart_items = models.Cart.objects.filter(user_id=user_id, has_check=1)

    for items in commit_cart_items:
        items.has_check = 0
        items.save()


def pay_order_service():
    """
    订单支付服务
    :return:
    """
    pass


# TODO: 以下为商品服务

def get_all_commodity_service(request):
    """
    获取商品列表服务
    :return: 返回商品列表
    """

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    all_commoditys = models.Commodity.objects.all()
    p = Paginator(all_commoditys, PER_PAGE_NUM, request=request)
    commoditys = p.page(page)
    return commoditys


def get_commodity_detail_service(commodity_id):
    """
    获取商品详情服务
    :return: 返回商品和商品信息
    """
    commodity = models.Commodity.objects.get(pk=commodity_id)
    commodity_info = models.CommodityInfo.objects.get(commodity_id=commodity_id).commodity_info.replace('\'', '').split(
        ',')

    return commodity, commodity_info


def take_coupon_service(user_id, type):
    """
    领取优惠券服务
    :param user_id:
    :param type:
    :return: 返回领取结果
    """
    strategies = models.PreferentialStrategy.objects.filter(type=type)
    coupons = models.Coupon.objects.filter(strategy_id=strategies[0].strategy_id, statue=1)
    coupon_list = list(coupons.all())
    if len(coupon_list) > 0:
        coupon = coupon_list[0]
        userToCoupon = models.UserToCoupon()
        userToCoupon.user_id = user_id
        userToCoupon.coupon_id = coupon.coupon_id
        userToCoupon.start_time = datetime.datetime.now()
        userToCoupon.end_time = userToCoupon.start_time + datetime.timedelta(days=coupon.expire_time)
        userToCoupon.save()
        coupon.statue = 2
        coupon.save()
        return True
    else:
        return False
