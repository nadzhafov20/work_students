# Generated by Django 5.0.4 on 2024-05-18 12:02

import django.contrib.auth.models
import django.utils.timezone
import timezone_field.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(blank=True, choices=[('student', 'Student'), ('client', 'Client')], max_length=20, null=True, verbose_name='Роль')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('time_zone', timezone_field.fields.TimeZoneField(blank=True, default='Asia/Dubai', null=True, verbose_name='Time zone')),
                ('verification_token', models.CharField(blank=True, max_length=100, null=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Balance')),
                ('about', models.TextField(blank=True, default='this account is still under development', max_length=1000, null=True, verbose_name='About')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images/', verbose_name='Image')),
                ('price_hour', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Price/hour')),
                ('hours_per_week', models.IntegerField(blank=True, null=True, verbose_name='Hours per week')),
                ('user_id_key', models.CharField(max_length=12, unique=True, verbose_name='ID key')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
