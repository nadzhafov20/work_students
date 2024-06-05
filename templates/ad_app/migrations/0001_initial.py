# Generated by Django 5.0.4 on 2024-06-04 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ad_images/', verbose_name='Image')),
                ('timer', models.PositiveIntegerField(default=1, verbose_name='Minuts')),
                ('link', models.URLField(verbose_name='URL')),
                ('placement', models.CharField(choices=[('home_page', 'Home page (200x150px)'), ('popup', 'Pop-up window'), ('bottom', 'Bottom'), ('block', 'Block'), ('profile', 'Profile (300x300px)'), ('header', 'Header (800x100px)'), ('right_block', 'Right (300x400px)'), ('sticky', 'Sticky (150x200px)')], max_length=40)),
                ('date_add', models.DateTimeField(auto_now=True, verbose_name='Date add')),
            ],
            options={
                'verbose_name': 'Advertisement',
                'verbose_name_plural': 'Advertisement',
            },
        ),
    ]
