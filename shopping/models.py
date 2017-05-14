from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


# Create your models here.




class Commodity(models.Model):
    """
    商品表
    """
    commodity_id = models.BigIntegerField(primary_key=True, null=False, verbose_name='商品 ID')
    title = models.CharField(max_length=200, null=False, default='', verbose_name='商品标题')
    subtitle = models.CharField(max_length=300, null=False, default='', verbose_name='商品副标题')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.0, verbose_name='价格')
    pic1 = models.CharField(max_length=500, null=False, default='', verbose_name='商品图片 1')
    pic2 = models.CharField(max_length=500, null=False, default='', verbose_name='商品图片 2')
    pic3 = models.CharField(max_length=500, null=False, default='', verbose_name='商品图片 3')
    # commodity_info = models.TextField(null=False, default='', verbose_name='商品出版信息')
    url = models.CharField(max_length=500, null=False, default='', verbose_name='商品链接')

    class Meta:
        db_table = 'commodity'
        verbose_name = '商品管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class CommodityInfo(models.Model):
    commodity_id = models.BigIntegerField(unique=True, primary_key=True,null=False, default=0, verbose_name='商品 ID')
    commodity_info = models.TextField(null=False, default='', verbose_name='商品出版信息')

    class Meta:
        db_table = 'commodity_info'
        verbose_name = '商品出版信息管理'
        verbose_name_plural = verbose_name


class User(AbstractUser):
    """
    用户表，使用 Django 自带的 AbstractUser
    """
    user_id = models.BigIntegerField(primary_key=True, auto_created=True, null=False, verbose_name='用户 ID')
    user_phone = models.CharField(max_length=16, null=False, default='', unique=True, verbose_name='用户电话')
    user_email = models.CharField(max_length=30, null=False, default='', unique=True, verbose_name='用户邮箱')
    update_time = models.DateTimeField(max_length=40, null=False, default=now, verbose_name='信息修改日期')

    class Meta:
        db_table = 'user'
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name


class ReciverInfo(models.Model):
    """
    收货地址信息
    """
    receiver_info_id = models.BigIntegerField(primary_key=True, auto_created=True, null=False, default=0,
                                              verbose_name='收货信息 ID')
    user_id = models.CharField(max_length=10, null=False, verbose_name='用户 ID')
    receiver = models.CharField(max_length=10, null=False, default='', verbose_name='收件人')
    area = models.TextField(null=False, verbose_name='收件地址')
    address_detail = models.TextField(null=False, verbose_name='地址详情')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=16, null=False, verbose_name='收件人电话')

    class Meta:
        db_table = 'receiver_info'
        verbose_name = '收货地址管理'
        verbose_name_plural = verbose_name


class Cart(models.Model):
    """
    购物车
    """
    # id = models.BigIntegerField(primary_key=True, auto_created=True, null=False, default=0)
    user_id = models.BigIntegerField(null=False, default=0, verbose_name='用户 ID')
    commodity_id = models.BigIntegerField(null=False, default=0, verbose_name='商品 ID')
    quantity = models.IntegerField(null=False, default=1, verbose_name='数量')

    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.0, verbose_name='商品单价')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.0, verbose_name='商品总价')
    title = models.TextField(null=False, default='')
    pic1 = models.TextField(null=False, default='')
    has_check = models.IntegerField(null=False, default=0, verbose_name='是否被选中进行结算')

    class Meta:
        db_table = 'cart'
        verbose_name = '购物车管理'
        verbose_name_plural = verbose_name


class Order(models.Model):
    """
    订单表
    """
    order_id = models.BigIntegerField(primary_key=True, null=False, auto_created=True, verbose_name='订单 ID')
    user_id = models.BigIntegerField(null=False, verbose_name='用户 ID')
    receiver_info_id = models.BigIntegerField(null=False, default=0, verbose_name='收货信息 ID')
    ctime = models.DateTimeField(null=False, default=now, verbose_name='创建时间')
    distribution_info_id = models.BigIntegerField(null=False, verbose_name='物流信息 ID')
    pay_info_id = models.BigIntegerField(null=False, verbose_name='支付信息ID')
    statue = models.SmallIntegerField(null=False, verbose_name='订单状态')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.0, verbose_name='订单总额')
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.0, verbose_name='折扣金额')

    class Meta:
        db_table = 'order'
        verbose_name = '订单管理'
        verbose_name_plural = verbose_name


class OrderCommodityItem(models.Model):
    """
    订单商品项表
    """

    order_id = models.BigIntegerField(null=False, verbose_name='订单 ID')
    commodity_id = models.BigIntegerField(null=False, verbose_name='商品 ID')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.0, verbose_name='订单商品价格')
    quantity = models.BigIntegerField(null=False, default=1, verbose_name='商品数量')

    class Meta:
        db_table = 'order_commodity'
        verbose_name = '订单商品管理'
        verbose_name_plural = verbose_name


class DeliveryInfo(models.Model):
    """
    物流信息表
    """
    distribution_info_id = models.BigIntegerField(primary_key=True, null=False, auto_created=True,
                                                  verbose_name='物流信息 ID')
    delivery_type = models.SmallIntegerField(null=False, default=1, verbose_name='快递类型')
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.0, verbose_name='运费')
    carrier = models.BigIntegerField(null=False, verbose_name='送货人')
    dtime = models.DateTimeField(null=False, default=now, verbose_name='生成时间')
    detail_info = models.TextField(null=False, verbose_name='详细信息')

    class Meta:
        db_table = 'delivery_info'
        verbose_name = '物流信息管理'
        verbose_name_plural = verbose_name


class PayInfo(models.Model):
    """
    支付详情表
    """
    pay_id = models.BigIntegerField(primary_key=True, null=False, auto_created=True, verbose_name='支付信息 ID')
    order_id = models.BigIntegerField(null=False, verbose_name='订单 ID')
    pay_way = models.SmallIntegerField(null=False, default=1, verbose_name='支付方式')
    commodity_total_parice = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.0,
                                                 verbose_name='商品总额')
    accounts_payable = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.0,
                                           verbose_name='应支付金额')
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.0, verbose_name='运费')
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.0, verbose_name='优惠金额')

    class Meta:
        db_table = 'pay_info'
        verbose_name = '支付详情管理'
        verbose_name_plural = verbose_name


class Coupon(models.Model):
    """
    优惠券表
    """
    coupon_id = models.BigIntegerField(primary_key=True, auto_created=True, null=False, verbose_name='优惠券 ID')
    strategy_id = models.BigIntegerField(null=False, verbose_name='优惠策略 ID')
    # 过期时间
    expire_time = models.IntegerField(null=False, default=0, verbose_name='过期时间')
    take_time = models.DateTimeField(null=False, default=now, verbose_name='领取时间')
    usage_time = models.DateTimeField(null=False, default=now, verbose_name='使用时间')
    # 未领取 1， 已领取未使用 2，已使用 3， 已过期 4
    statue = models.SmallIntegerField(null=False, default=0, verbose_name='使用状态')
    strategy_desc = models.CharField(max_length=120, null=False, default='', verbose_name='优惠券描述')
    strategy_type = models.SmallIntegerField(null=False, verbose_name='优惠券类型')

    class Meta:
        db_table = 'coupon'
        verbose_name = '优惠券管理'
        verbose_name_plural = verbose_name


class PreferentialStrategy(models.Model):
    """
    优惠策略表
    """
    strategy_id = models.BigIntegerField(primary_key=True, null=False, auto_created=True, verbose_name='优惠策略 ID')
    # 1 折扣  2 满减 3 满X送Y
    type = models.SmallIntegerField(null=False, verbose_name='优惠类型')
    # 0 - 100 代表打折百分比
    preferential_discount = models.IntegerField(null=False, default=100, verbose_name='折扣百分比')
    # 满减或者满送的起点金额, 类型为折扣时值为-1
    preferential_point = models.IntegerField(default=-1, null=False, verbose_name='满减满送起点金额')
    # 满减或者满送的优惠金额,类型为折扣时-1
    preferential_money = models.IntegerField(default=-1, null=False, verbose_name='满减满送优惠金额')
    description = models.CharField(max_length=120, null=False, default='', verbose_name='优惠策略描述信息')

    class Meta:
        db_table = 'preferential_strategy'
        verbose_name = '优惠策略管理'
        verbose_name_plural = verbose_name


class UserToCoupon(models.Model):
    """
    用户与优惠券关系表
    """
    user_id = models.BigIntegerField(null=False, verbose_name='用户 ID')
    coupon_id = models.BigIntegerField(null=False, unique=True, verbose_name='优惠券 ID')
    # 有效起止时间，根据有效日期和领取日期确定
    start_time = models.DateTimeField(null=False, default=now, verbose_name='有效起始日期')
    end_time = models.DateTimeField(null=False, default=now, verbose_name='有效截止日期')

    class Meta:
        db_table = 'user_to_coupon'
        verbose_name = '用户优惠券管理'
        verbose_name_plural = verbose_name
