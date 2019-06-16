from django import forms
from .models import Morador

class dadosForm(forms.ModelForm):
    
    class Meta:
        model = Morador
        fields = ('nome', 'condominio', 'apartamento')