from django import forms

class dostavka(forms.Form):
    name = forms.CharField()
    fam = forms.CharField()
    mail = forms.CharField()
    adres = forms.CharField()
