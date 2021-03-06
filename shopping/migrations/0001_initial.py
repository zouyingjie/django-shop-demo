# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 11:55
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='用户 ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_phone', models.CharField(default='', max_length=16, unique=True, verbose_name='用户电话')),
                ('user_email', models.CharField(default='', max_length=30, unique=True, verbose_name='用户邮箱')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, max_length=40, verbose_name='信息修改日期')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
                'verbose_name_plural': '用户管理',
                'verbose_name': '用户管理',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(default=0, verbose_name='用户 ID')),
                ('commodity_id', models.BigIntegerField(default=0, verbose_name='商品 ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='商品单价')),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='商品总价')),
                ('title', models.TextField(default='')),
                ('pic1', models.TextField(default='')),
                ('has_check', models.IntegerField(default=0, verbose_name='是否被选中进行结算')),
            ],
            options={
                'db_table': 'cart',
                'verbose_name_plural': '购物车管理',
                'verbose_name': '购物车管理',
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('commodity_id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='商品 ID')),
                ('title', models.TextField(default='', verbose_name='商品标题')),
                ('subtitle', models.TextField(default='', verbose_name='商品副标题')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='价格')),
                ('pic1', models.TextField(default='', verbose_name='商品图片 1')),
                ('pic2', models.TextField(default='', verbose_name='商品图片 2')),
                ('pic3', models.TextField(default='', verbose_name='商品图片 3')),
                ('commodity_info', models.TextField(default='', verbose_name='商品出版信息')),
                ('url', models.TextField(default='', verbose_name='商品链接')),
            ],
            options={
                'db_table': 'commodity',
                'verbose_name_plural': '商品管理',
                'verbose_name': '商品管理',
            },
        ),
        migrations.CreateModel(
            name='CommodityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity_id', models.BigIntegerField(default=0, unique=True, verbose_name='商品 ID')),
                ('commodity_info', models.TextField(default='', verbose_name='商品出版信息')),
            ],
            options={
                'db_table': 'commodity_info',
                'verbose_name_plural': '商品出版信息管理',
                'verbose_name': '商品出版信息管理',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('coupon_id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='优惠券 ID')),
                ('strategy_id', models.BigIntegerField(verbose_name='优惠策略 ID')),
                ('expire_time', models.IntegerField(default=0, verbose_name='过期时间')),
                ('take_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='领取时间')),
                ('usage_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='使用时间')),
                ('statue', models.SmallIntegerField(default=0, verbose_name='使用状态')),
                ('strategy_desc', models.CharField(default='', max_length=120, verbose_name='优惠券描述')),
                ('strategy_type', models.SmallIntegerField(verbose_name='优惠券类型')),
            ],
            options={
                'db_table': 'coupon',
                'verbose_name_plural': '优惠券管理',
                'verbose_name': '优惠券管理',
            },
        ),
        migrations.CreateModel(
            name='DeliveryInfo',
            fields=[
                ('distribution_info_id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='物流信息 ID')),
                ('delivery_type', models.SmallIntegerField(default=1, verbose_name='快递类型')),
                ('delivery_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='运费')),
                ('carrier', models.BigIntegerField(verbose_name='送货人')),
                ('dtime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='生成时间')),
                ('detail_info', models.TextField(verbose_name='详细信息')),
            ],
            options={
                'db_table': 'delivery_info',
                'verbose_name_plural': '物流信息管理',
                'verbose_name': '物流信息管理',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='订单 ID')),
                ('user_id', models.BigIntegerField(verbose_name='用户 ID')),
                ('receiver_info_id', models.BigIntegerField(default=0, verbose_name='收货信息 ID')),
                ('ctime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('distribution_info_id', models.BigIntegerField(verbose_name='物流信息 ID')),
                ('pay_info_id', models.BigIntegerField(verbose_name='支付信息ID')),
                ('statue', models.SmallIntegerField(verbose_name='订单状态')),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='订单总额')),
                ('discount_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='折扣金额')),
            ],
            options={
                'db_table': 'order',
                'verbose_name_plural': '订单管理',
                'verbose_name': '订单管理',
            },
        ),
        migrations.CreateModel(
            name='OrderCommodityItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.BigIntegerField(verbose_name='订单 ID')),
                ('commodity_id', models.BigIntegerField(verbose_name='商品 ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='订单商品价格')),
                ('quantity', models.BigIntegerField(default=1, verbose_name='商品数量')),
            ],
            options={
                'db_table': 'order_commodity',
                'verbose_name_plural': '订单商品管理',
                'verbose_name': '订单商品管理',
            },
        ),
        migrations.CreateModel(
            name='PayInfo',
            fields=[
                ('pay_id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='支付信息 ID')),
                ('order_id', models.BigIntegerField(verbose_name='订单 ID')),
                ('pay_way', models.SmallIntegerField(default=1, verbose_name='支付方式')),
                ('commodity_total_parice', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='商品总额')),
                ('accounts_payable', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='应支付金额')),
                ('delivery_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='运费')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='优惠金额')),
            ],
            options={
                'db_table': 'pay_info',
                'verbose_name_plural': '支付详情管理',
                'verbose_name': '支付详情管理',
            },
        ),
        migrations.CreateModel(
            name='PreferentialStrategy',
            fields=[
                ('strategy_id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='优惠策略 ID')),
                ('type', models.SmallIntegerField(verbose_name='优惠类型')),
                ('preferential_discount', models.IntegerField(default=100, verbose_name='折扣百分比')),
                ('preferential_point', models.IntegerField(default=-1, verbose_name='满减满送起点金额')),
                ('preferential_money', models.IntegerField(default=-1, verbose_name='满减满送优惠金额')),
                ('description', models.CharField(default='', max_length=120, verbose_name='优惠策略描述信息')),
            ],
            options={
                'db_table': 'preferential_strategy',
                'verbose_name_plural': '优惠策略管理',
                'verbose_name': '优惠策略管理',
            },
        ),
        migrations.CreateModel(
            name='ReciverInfo',
            fields=[
                ('receiver_info_id', models.BigIntegerField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='收货信息 ID')),
                ('user_id', models.CharField(max_length=10, verbose_name='用户 ID')),
                ('receiver', models.CharField(default='', max_length=10, verbose_name='收件人')),
                ('area', models.TextField(verbose_name='收件地址')),
                ('address_detail', models.TextField(verbose_name='地址详情')),
                ('zip_code', models.CharField(max_length=6, null=True, verbose_name='邮政编码')),
                ('phone', models.CharField(max_length=16, verbose_name='收件人电话')),
            ],
            options={
                'db_table': 'receiver_info',
                'verbose_name_plural': '收货地址管理',
                'verbose_name': '收货地址管理',
            },
        ),
        migrations.CreateModel(
            name='UserToCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(verbose_name='用户 ID')),
                ('coupon_id', models.BigIntegerField(unique=True, verbose_name='优惠券 ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='有效起始日期')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='有效截止日期')),
            ],
            options={
                'db_table': 'user_to_coupon',
                'verbose_name_plural': '用户优惠券管理',
                'verbose_name': '用户优惠券管理',
            },
        ),
    ]
