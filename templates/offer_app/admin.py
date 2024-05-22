from django.contrib import admin
from .models import OffersModel, TagOfferModel, RatesOfferModel, MessagesOfferModel
from datetime import datetime, timedelta


class RatesOfferInline(admin.StackedInline):
    model = RatesOfferModel
    extra = 1
    readonly_fields = ('offer', 'student', 'date_add', 'text',)

class MessagesOfferInline(admin.StackedInline):
    model = MessagesOfferModel
    extra = 0
    readonly_fields = ('from_user','message')

class OffersAdmin(admin.ModelAdmin):
    inlines = [MessagesOfferInline, RatesOfferInline]
    readonly_fields = ('user_client', 'user_student', 'title', 'description', 'date_add', 'tags', 'spent', 'status', )

admin.site.register(OffersModel, OffersAdmin)
admin.site.register(TagOfferModel)