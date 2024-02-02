# Generated by Django 4.2.7 on 2024-02-01 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('price', models.IntegerField()),
                ('stripe_session_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='payhistory',
            name='payment_for',
        ),
        migrations.RemoveField(
            model_name='payhistory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='user_membership',
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='membership',
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='user',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='PayHistory',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
        migrations.DeleteModel(
            name='UserMembership',
        ),
    ]