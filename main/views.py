from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Coupon, Company, CartItem
from .tasks import send_cart_item_added_email

class HomePage(ListView):
    model = Coupon
    template_name = "main/home_page.html"
    context_object_name = "coupons"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['cart_coupons'] = CartItem.objects.select_related('user', 'coupon').filter(user=self.request.user).values_list(
                'coupon__id', flat=True)
        else:
            context['cart_coupons'] = []
        return context

    def get_queryset(self):
        return super().get_queryset().select_related('company')


class CompaniesList(ListView):
    model = Company
    template_name = "main/companies.html"
    context_object_name = "companies"
    paginate_by = 3


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, coupon_id):
        coupon = Coupon.objects.get(id=coupon_id)
        user = request.user
        user_cart_count = CartItem.objects.select_related('user').filter(user=user).count()
        if user_cart_count >= user.coupon_limit:
            return HttpResponse("Coupon limit reached for this user")
        user.coupon_limit = F("coupon_limit")-1
        user.save()

        if coupon.limit <= 0:
            coupon.claimed = True
            return HttpResponse("Coupon limit reached")
        Coupon.objects.filter(id=coupon_id).update(limit=F('limit') - 1)
        coupon.save()
        cart_item, created = CartItem.objects.select_related('coupon', 'user').get_or_create(
            coupon=coupon, user=request.user
        )
        cart_item.save()

        send_cart_item_added_email.apply_async(request.user.id, cart_item.id)

        return redirect('main:view_cart')


class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, claimed_coupon_id):
        cart_item = CartItem.objects.select_related('coupon', 'user').get(id=claimed_coupon_id)
        user = request.user
        related_coupon = cart_item.coupon
        cart_item.delete()
        user.coupon_limit = F("coupon_limit") - 1
        related_coupon.limit = F('limit') + 1
        related_coupon.save()

        send_cart_item_remove_email.apply_async(request.user.id)
        return redirect('main:home')


class CartView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = 'main/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


class CompanyDetailView(DetailView):
    model = Company
    context_object_name = 'company'
    template_name = 'main/company_detail.html'
    pk_url_kwarg = 'pk'
