from django import forms
from .models import Bankform
class AccregForm(forms.ModelForm):
	FIRSTNAME = forms.CharField()
	LASTNAME = forms.CharField()
	ADDRESS = forms.CharField()
	AGE = forms.IntegerField()
	DOB = forms.DateField()
	BRANCH = forms.CharField()
	PHONENO = forms.IntegerField()
	EMAIL = forms.EmailField()
class AccregForm(forms.ModelForm):
	    class Meta:
	        model = Bankform
	        fields = ('FIRSTNAME','LASTNAME','ADDRESS','AGE','DOB','BRANCH','PHONENO','EMAIL')
	    	