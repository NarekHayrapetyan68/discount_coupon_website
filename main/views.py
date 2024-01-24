from django.views.generic import ListView
from .models import Coupon, Company


class HomePage(ListView):
    model = Coupon
    template_name = "main/home_page.html"
    context_object_name = "coupons"


class CompaniesList(ListView):
    model = Company
    template_name = "main/companies.html"
    context_object_name = "companies"
