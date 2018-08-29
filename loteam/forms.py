from django import forms

class NameForm(forms.Form):
    name=forms.CharField(label='Your name', max_length=100)
    email=forms.CharField(label='Your email', max_length=100)