from django import forms
from main.models import MyUser
from .models import PortfolioStudentModel, EducationStudentModel, LanguageStudentModel, SetQualificationStudentModel
from django.contrib.auth.hashers import make_password
from django.forms.widgets import ClearableFileInput


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
        widgets = {
            'text': forms.TextInput(attrs={'class': 'custom-edit-input__active'}),
        }

class LanguageStudentForm(forms.ModelForm):
    class Meta:
        model = LanguageStudentModel
        fields = ['language', 'level']
        #widgets = {
        #    'language':
        #    'level':
        #}

class CustomClearableFileInput(ClearableFileInput):
    template_name = 'custom_clearable_file_input.html'


    def __init__(self, *args, **kwargs):
        self.id = kwargs.pop('id', None)
        super().__init__(*args, **kwargs)
        self.attrs.update({'class': 'custom-edit-input__active'})
    
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'id': self.id,
        })
        print(self.id)
        return context
    
    def use_template(self, name=None):
        return name == 'template_with_initial' or super().use_template(name)

class PersonalinfoSettingForm(forms.ModelForm):
    education_formset = forms.inlineformset_factory(
        MyUser,
        EducationStudentModel,
        form=EducationStudentForm,
        extra=1,
        can_delete=True
    )
    language_formset = forms.inlineformset_factory(
        MyUser,
        LanguageStudentModel,
        form=LanguageStudentForm,
        extra=1,
        can_delete=True
    )

    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'custom-edit-input__active'})
    )
    class Meta:
        model = MyUser
        fields = ('qualification', 'hours_per_week', 'price_hour', 'address', 'video_introduction', 'time_zone', 'about', 'skils', 'image', 'new_password')
        widgets = {
            'skils': forms.CheckboxSelectMultiple(),
            'image': CustomClearableFileInput(attrs={'class': 'custom-checkbox'})
        }

    def __init__(self, *args, **kwargs):
        user = super(PersonalinfoSettingForm, self).__init__(*args, **kwargs)
        self.fields['qualification'].queryset = SetQualificationStudentModel.objects.all()

        
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