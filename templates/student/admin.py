from django.contrib import admin
from .models import SetStudentSkilsModel, SetQualificationStudentModel


class SetStudentSkilsAdmin(admin.ModelAdmin):
    model = SetStudentSkilsModel


admin.site.register(SetStudentSkilsModel)
admin.site.register(SetQualificationStudentModel)