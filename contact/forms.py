from django import forms
from .models import Signup


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-light'
            field.widget.attrs['placeholder'] = field.label.title()