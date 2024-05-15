from django.contrib import admin
from .models import OffersModel, TagOfferModel, RatesOfferModel


class RatesOfferInline(admin.StackedInline):
    model = RatesOfferModel
    extra = 1

class OffersAdmin(admin.ModelAdmin):
    inlines = [RatesOfferInline]

admin.site.register(OffersModel, OffersAdmin)
admin.site.register(TagOfferModel)