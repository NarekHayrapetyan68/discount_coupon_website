from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_login', 'user_coupon', 'is_active', 'is_staff')
    list_filter = ('last_login', 'is_active')

    @staticmethod
    def user_coupon(obj):
        return obj.user_coupon.count()

    user_coupon.short_description = 'Claimed coupons'


admin.site.register(User, UserAdmin)
