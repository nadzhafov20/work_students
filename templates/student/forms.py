from django import forms
from main.models import MyUser
from .models import PortfolioStudentModel


class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) 

    class Meta:
        model = MyUser
        fields = ('email', 'phone_number', 'first_name', 'last_name', 'role', 'password')
        widgets = {'role': forms.HiddenInput()}

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = PortfolioStudentModel
        fields = ['title', 'description', 'image']