from django import forms
from portfolio.models import person

class personform(forms.ModelForm):
    class Meta:
        model =person
        #fields = ['first_name','last_name']
        exclude = ('status',)