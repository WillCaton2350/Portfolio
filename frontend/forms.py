from django import forms
from .models import portfolioModels

class ContactForm(forms.ModelForm):
    class Meta:
        model = portfolioModels
        fields = "__all__"