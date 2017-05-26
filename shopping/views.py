from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render_to_response

from shopping.forms import RegisterForm, LoginForm
from shopping import service


# Create your views here.


# TODO: 商品界面请求处理
class CommodityDetailView(View):
    """
    商品详情
    """

    def get(self, request, commodity_id):
        commodity, commodity_info = service.get_commodity_detail_service(commodity_id)
        return render(request, 'commodity_detail.html', {'commodity': commodity, 'commodity_info': commodity_info, })


class CommodityListView(View):
    """
    商品列表
    """

    def get(self, request):
        commodities = service.get_all_commodity_service(request)
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                user_id = request.user.user_id
                cart_items = service.check_cart_record_service(user_id)
                return render(request, 'commodity_list.html', {'commodities': commodities, 'cart_items': cart_items, })

        return render(request, 'commodity_list.html', {'commodities': commodities, 'cart_items': {}, })


# TODO: 用户登录注册请求处理
class LoginView(View):
    """
    登录
    """

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = request.POST.get("user_email", "")
            password = request.POST.get("password", "")
            user = authenticate(request, username=user_email, password=password)

            if user is not None:
                service.login(request, user)
                return HttpResponseRedirect(reverse("shopping:commodity_list"))

            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form})


class LogoutView(View):
    """
    注销登录
    """

    def get(self, request):
        service.logout(request)
        return HttpResponseRedirect(reverse("shopping:commodity_list"))


class RegisterView(View):
    """
    注册
    """

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            service.register_service(request)
            return render(request, 'login.html')

        else:
            return render(request, 'register.html', {'register_form': register_form})


# TODO: 购物车相关请求处理
class MyCartView(View):
    def get(self, request):

        data = dict()
        if request.user.is_authenticated():
            if not request.user.is_superuser:
                user_id = request.user.user_id
                cart_items = service.check_cart_record_service(user_id)
                data['cart_items'] = cart_items
                return render(request, 'my_cart.html', data)
            else:
                service.logout(request)
        return HttpResponseRedirect(reverse("shopping:login"))


class AddToCartView(View):
    """
    添加商品项到购物车
    """

    def post(self, request):
        if request.user.is_authenticated():
            user_id = request.user.user_id
            commodity_id = request.POST.get('commodity_id')

            service.add_to_cart_service(commodity_id, user_id)

            return JsonResponse({'statue': 'success'})
        else:
            return render(request, 'login.html')


class DeleteFromCartView(View):
    """
    从购物车删除商品
    """

    def post(self, request):
        user_id = request.user.user_id
        commodity_id = request.POST.get('commodity_id')
        service.delete_cart_commodity_service(user_id, commodity_id)
        return JsonResponse({"statues": 'success'})


# TODO:参考京东，待开发订单详情界面
class OrderView(View):
    def get(self, request):
        return HttpResponse('Order')

    def post(self, request):
        return HttpResponse('Order')


class AccountView(View):
    """
    结算
    将选中的购物车项设置 has_check=1,代表被选中进行结算，取消的话恢复为0
    """

    def post(self, request):
        cart_item_ids = request.POST.get('cart_items').split(',')
        service.cart_account_service(cart_item_ids)
        return HttpResponseRedirect(reverse("shopping:order_commit_page"))


class OrderCommitPageView(View):
    """
    订单提交操作界面
    """

    def get(self, request):
        if request.user.is_authenticated:
            if not request.user.is_superuser:

                # 选出用户购物车中已经被选中的数据项
                user_id = request.user.user_id
                commit_cart_items, coupons = service.commit_order_page_service(user_id)
                return render(request, 'order_commit_page.html', {'cart_items': commit_cart_items, 'coupons': coupons})
            else:
                service.logout(request)

        return HttpResponseRedirect(reverse("shopping:login"))


class OrderCommitOperationView(View):
    """
    执行订单提交
    """

    def post(self, request):
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                user_id = request.user.user_id
                coupon_id = request.POST.get('coupon_id', '')
                total_price = request.POST.get('total_price', '')
                discount_price = request.POST.get('discount_price', '')

                service.generate_order_service(user_id, coupon_id, total_price, discount_price)
                return HttpResponseRedirect(reverse("shopping:order_commit_success"))
            else:
                service.logout(request)

        return HttpResponseRedirect(reverse("shopping:login"))


class OrderCommitSuccessView(View):
    """
    订单提交成功跳转
    """

    def get(self, request):
        return render(request, "order_commit_success.html")


class OrderCancelOperationView(View):
    """
    订单取消操作
    """

    def get(self, request):
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                # 选出用户购物车中已经被选中的数据项
                user_id = request.user.user_id
                service.cancel_order_service(user_id)
                return HttpResponseRedirect(reverse("shopping:my_cart"))
            else:
                service.logout(request)
        return HttpResponseRedirect(reverse("shopping:login"))


class ChangeCartItemQuantityView(View):
    def post(self, request):
        commodity_id = request.POST['commodity_id']
        quantity = request.POST['quantity']

        user_id = request.user.user_id
        cart_item = service.change_cart_quantity_service(user_id, commodity_id, quantity)
        return JsonResponse({'price': cart_item.total_price})


# TODO:购物券相关请求处理
class CouponPageView(View):
    """
    优惠券界面
    """

    def get(self, request):
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                return render(request, 'coupon.html')
            else:
                service.logout(request)

        return HttpResponseRedirect(reverse("shopping:login"))


class TakeCouponViw(View):
    """
    领取购物券操作
    """

    def post(self, request):

        if request.user.is_authenticated:
            coupon_type = request.POST.get('coupon_type', "")
            if service.take_coupon_service(request.user.user_id, coupon_type):
                return JsonResponse({'statue': '200'})

        return JsonResponse({'statue': '404'})


# 全局 404 配置
def page_not_found(request):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


# 全局 500 配置
def page_error(request):
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
