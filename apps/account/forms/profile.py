from django import forms
from account.models import User, EmployeeProfile, EmployerProfile

class EmployeeProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter Last Name'})
        for field in self.fields.values():
            field.required = False

    class Meta:
        model = User
        fields = ["first_name", "last_name", "gender"]

class EmployeeProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
            existing_class = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_class} form-control'.strip()

    class Meta:
        model = EmployeeProfile
        fields = ["resume", "location", "phone_number", "bio", "skills"]
        widgets = {
            'location': forms.TextInput(attrs={'placeholder': 'City, State or Country'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about yourself...'}),
        }

class EmployerProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployerProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
            existing_class = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_class} form-control'.strip()

    class Meta:
        model = EmployerProfile
        fields = ["company_location", "company_website", "company_logo", "description"]
        widgets = {
            'company_location': forms.TextInput(attrs={'placeholder': 'City, State or Country'}),
            'company_website': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about your company...'}),
        }
