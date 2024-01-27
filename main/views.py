from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductFilterForm
from django.views.generic import ListView, FormView
from .models import Coupon, Company, CartItem


class HomePage(ListView):
    model = Coupon
    template_name = "main/home_page.html"
    context_object_name = "coupons"

    def get_queryset(self):
        return super().get_queryset().select_related('company')


class CompaniesList(ListView):
    model = Company
    template_name = "main/companies.html"
    context_object_name = "companies"


class FilterView(FormView):
    template_name = "main/filter.html"
    form_class = ProductFilterForm


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, coupon_id):
        coupon = Coupon.objects.get(id=coupon_id)
        if coupon.limit <= 0:
            coupon.claimed = True
            return HttpResponse("Coupon limit reached")
        coupon.limit -= 1
        coupon.save()
        cart_item, created = CartItem.objects.select_related('coupon', 'user').get_or_create(
            coupon=coupon, user=request.user
        )
        cart_item.quantity += 1
        cart_item.save()
        return redirect('main:view_cart')
    #change to  F class


class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, claimed_coupon_id):
        cart_item = CartItem.objects.select_related('coupon', 'user').get(id=claimed_coupon_id)
        cart_item.delete()
        return redirect('main:view_cart')


class CartView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = 'main/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)