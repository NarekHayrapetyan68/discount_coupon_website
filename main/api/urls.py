from django.urls import path

from .views import CouponListCreateAPIView, ListCompanyAPIView

urlpatterns = [
    path("<int:company_pk>/", CouponListCreateAPIView.as_view()),
    path("companies/", ListCompanyAPIView.as_view()),
]
