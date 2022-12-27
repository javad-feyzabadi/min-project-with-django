from . models import LessionScore
from django import forms

class LessionForm(forms.ModelForm):
    class Meta:
        model = LessionScore
        fields = '__all__' 