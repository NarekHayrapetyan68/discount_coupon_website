# Generated by Django 4.2.7 on 2024-02-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_cartitem_coupon_alter_cartitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='hot_offer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
