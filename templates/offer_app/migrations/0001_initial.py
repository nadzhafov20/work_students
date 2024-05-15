# Generated by Django 5.0.4 on 2024-05-15 17:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TagOfferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tag Name')),
            ],
            options={
                'verbose_name': 'Tag offer',
                'verbose_name_plural': 'Tags offer',
            },
        ),
        migrations.CreateModel(
            name='OffersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('date_add', models.DateTimeField(auto_now=True, verbose_name='Datetime add')),
                ('date_end', models.DateTimeField(blank=True, help_text='Leave blank if time is unlimited', null=True, verbose_name='Datetime end')),
                ('spent', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Spent')),
                ('status', models.CharField(blank=True, choices=[('awaits', 'Waiting'), ('launched', 'Launched'), ('completed', 'Completed')], max_length=20, null=True, verbose_name='Status')),
                ('user_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_offers', to=settings.AUTH_USER_MODEL, verbose_name='Client')),
                ('user_student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_offers', to=settings.AUTH_USER_MODEL, verbose_name='Student')),
                ('tags', models.ManyToManyField(to='offer_app.tagoffermodel', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offer',
            },
        ),
        migrations.CreateModel(
            name='RatesOfferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now=True, verbose_name='Date add')),
                ('text', models.TextField(max_length=2000, verbose_name='Text')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer_app.offersmodel', verbose_name='Offer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Student')),
            ],
            options={
                'verbose_name': 'Rate',
                'verbose_name_plural': 'Rates',
            },
        ),
    ]
