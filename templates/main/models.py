from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from student.models import SetStudentSkilsModel, SetQualificationStudentModel
from django.utils.text import slugify
from timezone_field import TimeZoneField



class MyUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('client', 'Client'),
    )
    email = models.EmailField(
        unique=True
    )
    phone_number = models.CharField(
        unique=True,
        blank=True,
        null=True,
        max_length=20
    )
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=100
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=100
    )
    role = models.CharField(
        blank=True,
        null=True,
        max_length=20,
        choices=ROLE_CHOICES,
        verbose_name='Роль'
    )
    email_verified = models.BooleanField(
        default=False,
        verbose_name='Email verified'
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        )
    address = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name='Address'
    )
    time_zone = TimeZoneField(
        null=True,
        blank=True,
        default="Asia/Dubai",
        verbose_name='Time zone'
    )
    verification_token = models.CharField(
        max_length=100, 
        null=True, 
        blank=True
    )

    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Balance'
    )

    about = models.TextField(
        null=True,
        blank=True,
        default='this account is still under development',
        max_length=1000,
        verbose_name='About'
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='profile_images/',
        verbose_name='Image',
    )

    qualification = models.ForeignKey(
        SetQualificationStudentModel,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Qualification'
    )

    price_hour = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Price/hour'
    )

    hours_per_week = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Hours per week'
    )
    skils= models.ManyToManyField(
        SetStudentSkilsModel,
        verbose_name='Skils'
    )

    user_id_key = models.CharField(
        unique=True,
        max_length=12,
        verbose_name='ID key'
    )


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if not self.username and not self.pk:
            base_username = slugify(f"{self.first_name}{self.last_name}")
            unique_username = base_username
            counter = 1
            while MyUser.objects.filter(username=unique_username).exists():
                unique_username = f"{base_username}{counter}"
                counter += 1
            self.username = unique_username
        super().save(*args, **kwargs)