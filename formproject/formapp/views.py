from django.shortcuts import render
from .forms import Candidatereg

# Create your views here.
def candreg(request):
	form=Candidatereg()
	return render(request,'formapp/display.html',context={'form':form})
