from django import forms
from .models import Preference
from django.core.exceptions import ValidationError

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields  = '__all__'


    # validating some of the fields in Preference model
    def clean_first_name(self):
        # if first name contains these special characters raise an error message

        first_name = self.cleaned_data.get('first_name')
        if '@' in  first_name:
            raise ValidationError(' name must not contain special characters')
        return first_name

