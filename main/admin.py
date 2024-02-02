from django.contrib import admin
from django.utils.html import format_html

from .models import Company, Coupon, CartItem


class CouponAdmin(admin.ModelAdmin):
    list_display = ('company', 'discount', 'limit', 'expire_date', 'claimed')
    search_fields = ('company',)
    list_filter = ('expire_date', 'claimed')

    @staticmethod
    def discount(obj):
        if obj.discount_price:
            return f'{obj.discount_price}$'
        else:
            return f'{obj.discount_percent}%'

    discount.short_description = 'Discount'


admin.site.register(Coupon, CouponAdmin)


class AdminCompany(admin.ModelAdmin):
    list_display = ('image', 'name', 'coupon', 'type',)
    list_filter = ('type',)
    search_fields = ('name',)
    list_display_links = ("image", "name")


    @staticmethod
    def image(obj):
        return format_html("<img src='{}' width='60'>", obj.image.url if obj.image else None)

    @staticmethod
    def coupon(obj):
        return obj.coupons.count()

    coupon.short_description = 'Claimed coupons'

    image.short_description = 'image'


admin.site.register(Company, AdminCompany)


class AdminCartItem(admin.ModelAdmin):
    list_display = ('user', 'company',)
    search_fields = ('company',)


    @staticmethod
    def company(obj):
        return obj.coupon.company

    company.short_description = 'company'


admin.site.register(CartItem, AdminCartItem)
