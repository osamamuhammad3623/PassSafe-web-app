from django import forms
from .models import contact

class contactForm(forms.Form):
    class Meta:
        model = contact
        fields = ['name', 'email', 'message']