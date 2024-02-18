from django.urls import path

from .views import CouponListCreateAPIView, ListCompanyAPIView, CompanyRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("company_coupon/<int:company_pk>/", CouponListCreateAPIView.as_view()),
    path("companies/<int:id>/", CompanyRetrieveUpdateDestroyAPIView.as_view()),
    path("companies/", ListCompanyAPIView.as_view()),
]
