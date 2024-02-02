from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.IntegerField()
    stripe_session_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

