from django import forms
from .models import RatesOfferModel, MessagesOfferModel


class RateForm(forms.ModelForm):
    class Meta:
        model = RatesOfferModel
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }

class MessagesOfferForm(forms.ModelForm):
    class Meta:
        model = MessagesOfferModel
        fields = ('message', )
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message here'}),
        }