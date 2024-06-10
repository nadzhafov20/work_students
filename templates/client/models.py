from django.db import models
from main.models import MyUser


class OfferJobModel(models.Model):
    STATUS_CHOICES = [
        ('confirmed', '✅ Confirmed'),
        ('rejected', '❌ Rejected'),
        ('awaits', '⏳ Awaits')
    ]
    user_client = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='offer_job_client_offers',
        verbose_name='Client'
    )
    user_student = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='offer_job_student_offers',
        verbose_name='Student',
    )
    text = models.TextField(
        max_length=2000,
        verbose_name='Text'
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Amount'
    )
    contacts = models.TextField(
        max_length=200,
        verbose_name='Contacts'
    )
    date_add = models.DateTimeField(
        auto_now=True,
        verbose_name='Date add'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='awaits'
    )
    def __str__(self):
        return str(self.date_add)
    class Meta:
        verbose_name = 'offer job'
        verbose_name_plural = 'offer jobs'