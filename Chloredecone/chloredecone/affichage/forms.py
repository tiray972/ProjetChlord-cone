from dataclasses import field, fields
from pyexpat import model
from socket import fromshare
from django import forms
from .models import summary_pdf





class ContactUsForm(forms.Form):
    name=forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
class RechercheForm(forms.Form):
    data=forms.CharField(required=False)

    
class summary_pdf(forms.ModelForm):
    class Meta:
        model=summary_pdf
        fields=("titre","file")

