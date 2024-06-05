from django import forms
from main.models import MyUser
from offer_app.models import OffersModel, TagOfferModel
from django.contrib.auth.hashers import make_password


class OffersModelForm(forms.ModelForm):
    class Meta:
        model = OffersModel
        fields = ('spent', 'tags', 'description', 'title')
        widgets = {
            'spent': forms.NumberInput(attrs={'class': 'spent-form'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'tags-form'}),
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
    

class PersonalinfoSettingForm(forms.ModelForm):
    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'custom-edit-input__active'})
    )

    class Meta:
        model = MyUser
        fields = ('address', 'time_zone', 'image', 'new_password')
        widgets = {
            'skils': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        user = super(PersonalinfoSettingForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'custom-edit-input__active'
    
    def save(self, commit=True):
        user = super(PersonalinfoSettingForm, self).save(commit=False)
        new_password = self.cleaned_data.get('new_password')
        if new_password:
            user.password = make_password(new_password)
        if commit:
            user.save()

        return user