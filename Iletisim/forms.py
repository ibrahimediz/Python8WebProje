from django import forms

from .models import iletisim

class iletisimForm(forms.ModelForm):

    class Meta:
        model = iletisim
        fields = ('Adı', 'soyAdı','email','giris',)