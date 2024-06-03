from django.contrib import admin
from .models import AdModel


class AdAdmin(admin.ModelAdmin):
    model = AdModel
    list_display = ('title', 'placement', 'timer', 'date_add')
    search_fields = ('title', 'placement', 'timer', 'date_add')

admin.site.register(AdModel, AdAdmin)