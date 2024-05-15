from django import forms
from .models import RatesOfferModel


class RateForm(forms.ModelForm):
    class Meta:
        model = RatesOfferModel
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }