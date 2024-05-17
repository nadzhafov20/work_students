from django import forms
from main.models import MyUser
from .models import PortfolioStudentModel, EducationStudentModel, LanguageStudentModel, SetQualificationStudentModel


class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) 

    class Meta:
        model = MyUser
        fields = ('email', 'phone_number', 'first_name', 'last_name', 'role', 'password')
        widgets = {'role': forms.HiddenInput()}

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = PortfolioStudentModel
        fields = ['title', 'description', 'photo']

class EducationStudentForm(forms.ModelForm):
    class Meta:
        model = EducationStudentModel
        fields = ['text']

class PersonalinfoSettingForm(forms.ModelForm):
    education_formset = forms.inlineformset_factory(
        MyUser,
        EducationStudentModel,
        form=EducationStudentForm,
        extra=1,
        can_delete=True
    )

    class Meta:
        model = MyUser
        fields = ('qualification', 'hours_per_week', 'price_hour', 'address', 'time_zone', 'password', 'about', 'skils', 'image')
        widgets = {
            'skils': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(PersonalinfoSettingForm, self).__init__(*args, **kwargs)
        self.fields['qualification'].queryset = SetQualificationStudentModel.objects.all()

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'custom-edit-input__active'

        def get_education_formset(self, *args, **kwargs):
            return self.education_formset(*args, **kwargs)