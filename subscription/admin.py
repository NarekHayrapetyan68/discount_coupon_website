from django.contrib import admin

from django.contrib import admin
from .models import Account

#
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ("name", "description", "price")
#     search_fields = ("name",)
#
#     fieldsets = (
#         (
#             "GENERAL",
#             {"fields": ("name", "description")},
#         ),
#         (
#             "INFO",
#             {
#                 "fields": (
#                     "price",
#                     "stripe_id",
#
#                 )
#             },
#         ),
#     )


admin.site.register(Account)
