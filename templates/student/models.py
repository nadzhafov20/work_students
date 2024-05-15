from django.db import models
import uuid


class SetStudentSkilsModel(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Skill'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skil'
        verbose_name_plural = 'Skills'

class SetQualificationStudentModel(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Qualification'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Qualification'
        verbose_name_plural = 'Qualifications'

class EducationStudentModel(models.Model):
    from main.models import MyUser

    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    text = models.CharField(
        max_length=100,
        verbose_name='Education'
    )
    
    def __str__(self):
        return 'Education'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'


class LanguageStudentModel(models.Model):
    from main.models import MyUser

    LANGUAGE = [
        ('English', 'English'),
        ('Spanish', 'Spanish'),
        ('French', 'French'),
        ('German', 'German'),
        ('Chinese', 'Chinese'),
    ]
    LEVEL = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Fluent', 'Fluent'),
    ]

    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    language = models.CharField(
        max_length=50,
        choices=LANGUAGE
    )
    level = models.CharField(
        max_length=50,
        choices=LEVEL
    )

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Language'


class StudentCalendarModel(models.Model):
    from main.models import MyUser

    STATUS = [
        ('red', 'Сильно занят'),
        ('yellow', 'Немного занят'),
    ]
    
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name='User'
    )

    date = models.DateField(
        verbose_name='Дата'
    )

    status = models.CharField(
        null=True,
        blank=True,
        max_length=30,
        choices=STATUS,
        verbose_name='Status'
    )

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Calendar'
        verbose_name_plural = 'Calendar'

class PortfolioStudentModel(models.Model):
    from main.models import MyUser
    
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        verbose_name='User'
    )

    photo = models.ImageField(
        upload_to='portfolio/',
        blank=True,
        null=True,
        verbose_name='Photo'
    )
    title = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Title'
    )
    description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name='Description'
    )

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'