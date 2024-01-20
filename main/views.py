from django.shortcuts import render
from django.views.generic import ListView
from .models import Coupon


class HomePage(ListView):
    model = Coupon
    template_name = "main/home_page.html"
