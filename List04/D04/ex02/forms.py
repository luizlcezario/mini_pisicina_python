from django import forms

class MyForm(forms.Form):
    campo = forms.CharField(required= True)