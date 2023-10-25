from django import forms
from .models import Exhibition

class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = '__all__'
