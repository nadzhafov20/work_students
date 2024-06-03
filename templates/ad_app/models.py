from django.db import models



class AdModel(models.Model):
    PLACEMENT_CHOICES = (
        ('home_page', 'Home page (200x150px)'),
        ('popup', 'Pop-up window'),
        ('bottom', 'Bottom'),
        ('block', 'Block'),
        ('profile', 'Profile (300x300px)'),
        ('header', 'Header (800x100px)'),
        ('right_block', 'Right (300x400px)'),
        ('sticky', 'Sticky (150x200px)'),
    )

    title = models.CharField(
        max_length=100,
        verbose_name='Title',
    )
    image = models.ImageField(
        upload_to='ad_images/',
        blank=True,
        null=True,
        verbose_name='Image'
    )
    timer = models.PositiveIntegerField(
        default=1,
        verbose_name='Minuts'
    )
    link = models.URLField(
        verbose_name='URL'
    )
    placement = models.CharField(
        max_length=40,
        choices=PLACEMENT_CHOICES,
    )
    date_add = models.DateTimeField(
        auto_now=True,
        verbose_name='Date add'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisement'
    