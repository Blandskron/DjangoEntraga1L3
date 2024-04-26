from django import forms
from .models import Autor, Articulo 

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'
