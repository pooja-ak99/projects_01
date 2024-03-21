from django import forms
from ServiceApp.models import Category

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
