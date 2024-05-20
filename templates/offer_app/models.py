from django.db import models
from main.models import MyUser



class TagOfferModel(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Tag Name'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag offer'
        verbose_name_plural = 'Tags offer'
    

class OffersModel(models.Model):
    CHOICES_STATUS = [
        ('awaits', 'Waiting'),
        ('launched', 'Launched'),
        ('completed', 'Completed')
    ]
    user_client = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='client_offers',
        verbose_name='Client'
    )
    user_student = models.ForeignKey(
        MyUser,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='student_offers',
        verbose_name='Student',
    )
    title = models.CharField(
        max_length=80,
        verbose_name='Title'
    )
    description = models.TextField(
        max_length=500,
        verbose_name='Description'
    )
    date_add = models.DateTimeField(
        auto_now=True,
        verbose_name='Datetime add'
    )
    date_end = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Datetime end',
        help_text='Leave blank if time is unlimited' 
    )
    tags = models.ManyToManyField(
        TagOfferModel,
        verbose_name='Tags'
    )
    spent = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Spent'
    )
    status = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=CHOICES_STATUS,
        verbose_name='Status'
    )

    def __str__(self):
        return str(self.date_add)

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offer'


class RatesOfferModel(models.Model):
    offer = models.ForeignKey(
        OffersModel,
        on_delete=models.CASCADE,
        verbose_name='Offer'
    )
    student = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name='Student'
    )
    date_add = models.DateTimeField(
        auto_now=True,
        verbose_name='Date add'
    )
    text = models.TextField(
        max_length=2000,
        verbose_name='Text'
    )

    def __str__(self):
        return self.offer.title
    
    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'

class MessagesOfferModel(models.Model):
    offer = models.ForeignKey(
        OffersModel,
        on_delete=models.CASCADE,
        verbose_name='Offer'
    )
    from_user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    message = models.TextField(
        max_length=1000,
        verbose_name='Message'
    )
    date_sent = models.DateTimeField(
        auto_now=True,
        verbose_name='Datetime sent'
    )

    def __str__(self):
        return str(self.date_sent)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'