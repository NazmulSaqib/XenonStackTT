from tkinter import Widget
from django.forms import ModelForm
from django import forms 
from .models import ContactModel
from django.contrib.auth.models import User

class QureyForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields =('name', 'problem')

        
