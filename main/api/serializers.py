from rest_framework import serializers

from main.models import Company, Coupon


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    pizza = CouponSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        exclude = ("image",)
