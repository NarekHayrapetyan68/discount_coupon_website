from django.db import models
from django.core.exceptions import ValidationError
from core.models import User


def upload_company_images(instance, filename):
    return f"users/{instance.user.username}/{filename}"

# class Valod(models.TextChoices):
#     Clothing = 'Clothing','clothing '


class Company(models.Model):
    STATUS_CHOICES = (
        ('Clothing', 'clothing '),
        ('Electronics', 'electronics'),
        ('Food', 'food '),
        ('Home Services', 'home Services'),
    )

    type = models.CharField(max_length=100, choices=STATUS_CHOICES)
    name = models.CharField(max_length=100)
    opening_hours = models.CharField(max_length=20,
                                     help_text=' "9:00-23:00" or "around the clock".')
    image = models.ImageField(upload_to=upload_company_images, blank=True, null=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=30, unique=True)
    discount_percent = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    discount_price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='coupons')
    about = models.TextField(blank=True, max_length=200)
    expire_date = models.DateField()
    limit = models.DecimalField(max_digits=6, decimal_places=0)
    claimed = models.BooleanField(default=False)

    def __str__(self):
        return f"coupon_{self.pk}"

    def clean(self):
        super().clean()

        if not any([self.discount_percent, self.discount_price]):
            raise ValidationError("Discount price or Discount percent should be filled.")


class CartItem(models.Model):
    coupon = models.ForeignKey(Coupon, related_name='claimed_coupon',on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_coupon', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

