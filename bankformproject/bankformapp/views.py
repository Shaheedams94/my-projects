from django.shortcuts import render
from .forms import AccregForm
from .models import Bankform
from django.http import HttpResponse

# Create your views here.
def accregister(request):
	form=AccregForm()
	if request.method=='POST':
		form=AccregForm(request.POST)
		if form.is_valid:
			form.save()
			print('data got stored in database')
			return success(request)
	return render(request,'bankformapp/bankform.html',{'form':form})

def success(request):
	s1 = "<center><h1>Acc Details Uploaded Successfully</h1></center>"
	#s2="<center><h1>Acc Details Uploaded Successfully</h1></center>"
	return HttpResponse(s1)
	return see(request)
	return display(request)
	
def display(request):
	cand_list=Bankform.objects.all()

	#my_dict={'cand_list':cand_list}
	return render(request,'bankformapp/bankform1.html',{'candidate':cand_list})
def see(request):
	return render(request,'bankform/bankview.html')



