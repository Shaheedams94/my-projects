from django import forms
class Candidatereg(forms.Form):
    # TODO: Define form fields here
    FIRSTNAME = forms.CharField()
    LASTNAME = forms.CharField()
    ADRESS = forms.CharField()
    CLG = forms.CharField()
    MARKS = forms.IntegerField()
    DESIGNATION = forms.CharField()
