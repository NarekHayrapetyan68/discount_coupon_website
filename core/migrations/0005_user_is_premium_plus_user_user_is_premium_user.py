# Generated by Django 4.2.7 on 2024-02-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_user_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_premium_plus_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_premium_user',
            field=models.BooleanField(default=False),
        ),
    ]