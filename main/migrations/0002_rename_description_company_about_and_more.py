# Generated by Django 4.2.7 on 2024-01-19 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='description',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='coupon',
            old_name='description',
            new_name='about',
        ),
        migrations.AddField(
            model_name='coupon',
            name='claimed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='coupon',
            name='expire_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='opening_hours',
            field=models.CharField(help_text=' "9:00-23:00" or "around the clock".', max_length=20),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='limit',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True),
        ),
    ]