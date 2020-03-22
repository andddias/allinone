from django import forms
from django.forms import ModelForm
from .models import MyModel


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['upload', ]
