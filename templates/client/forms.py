from django import forms
from main.models import MyUser
from offer_app.models import OffersModel, TagOfferModel


class OffersModelForm(forms.ModelForm):
    class Meta:
        model = OffersModel
        fields = ('spent', 'tags', 'date_end', 'description', 'title')
        widgets = {
            'spent': forms.NumberInput(attrs={'class': 'spent-form'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'tags-form'}),
            'date_end': forms.DateInput(attrs={'class': 'date_end-form'}),
            'description': forms.Textarea(attrs={'class': 'description-form'}),
            'title': forms.TextInput(attrs={'class': 'title-form'}),
        }

    def save(self, commit=True, user=None):
        offer = super(OffersModelForm, self).save(commit=False)
        if user is not None:
            offer.user_client = user
        if commit:
            offer.save()
            self.save_m2m()
        return offer