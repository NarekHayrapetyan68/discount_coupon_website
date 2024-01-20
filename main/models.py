from django.db import models
from django.core.exceptions import ValidationError

def upload_company_images(instance, filename):
    return f"users/{instance.user.username}/{filename}"


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
    discount = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='coupons')
    about = models.TextField(blank=True, max_length=200)
    expire_date = models.DateField(blank=True,null=True)
    expire_time = models.TimeField(blank=True,null=True)
    limit = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    claimed = models.BooleanField(default=False)

    def __str__(self):
        return "coupon"

    def clean(self):
        super().clean()

        if not any([self.expire_date, self.expire_time, self.limit]):
            raise ValidationError("At least one of Expire date, Expire time, or Limit should be filled.")

    def save(self, *args, **kwargs):
        if self.limit is not None:
            self.limit -= 1
            if self.limit == 0:
                self.claimed = True
                self.limit = -1
        super().save(*args, **kwargs)
