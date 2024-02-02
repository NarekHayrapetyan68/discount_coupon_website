from django.urls import path
from .views import HomePage, CompaniesList, CompanyDetailView, \
    CartView, AddToCartView, RemoveFromCartView

app_name = "main"
urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("companies/", CompaniesList.as_view(), name="company"),
    path("cart/", CartView.as_view(), name="view_cart"),
    path("add/<int:coupon_id>/", AddToCartView.as_view(), name="add_to_cart"),
    path("remove/<int:claimed_coupon_id>/", RemoveFromCartView.as_view(), name="remove_from_cart"),
    path("companies/<int:pk>", CompanyDetailView.as_view(), name="company_detail")

]
