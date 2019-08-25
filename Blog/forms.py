from django import forms
from .models import Gonderi

class GonderiForm(forms.ModelForm):
    class Meta:
        model = Gonderi
        fields = ("baslik","metin")