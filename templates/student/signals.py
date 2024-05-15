from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import SetStudentSkilsModel, SetQualificationStudentModel


@receiver(post_migrate)
def create_initial_skills(sender, **kwargs):
    if sender.name == 'student':
        initial_skills = ['Python', 'ReactJS', 'Figma', 'C++', 'Adobe Photoshop']
        for skill_name in initial_skills:
            SetStudentSkilsModel.objects.get_or_create(name=skill_name)

@receiver(post_migrate)
def create_initial_qualification(sender, **kwargs):
    if sender.name == 'student':
        initial_qualification = ['Designer', 'Coder']
        for qualification_name in initial_qualification:
            SetQualificationStudentModel.objects.get_or_create(name=qualification_name)