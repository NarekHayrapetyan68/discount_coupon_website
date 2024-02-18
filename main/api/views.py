from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CompanySerializer, CouponSerializer
from main.models import Coupon, Company


class CouponListCreateAPIView(ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    def get_queryset(self):
        company_pk = self.kwargs.get("company_pk")
        return Coupon.objects.filter(company=company_pk)

    def perform_create(self, serializer):
        company_pk = self.kwargs.get("company_pk")
        company_instance = Company.objects.get(pk=company_pk)
        serializer.save(company=company_instance)


class ListCompanyAPIView(ListCreateAPIView):
    queryset = Company.objects.all().order_by("-pk")
    serializer_class = CompanySerializer


class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all().order_by("-pk")
    serializer_class = CompanySerializer
    lookup_field = "id"

