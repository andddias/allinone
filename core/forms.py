from django import forms
from .models import Livro, Arquivo


class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ('arquivo', )

        # widgets é importante para carregar vários arquivos
        widgets = {'arquivo': forms.ClearableFileInput(attrs={'multiple': True})}


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ('titulo', 'autor', 'pdf', 'capa')
