from django.shortcuts import render

# Create your views here.
def deposit(request):
	msg='client is depositing the amount'
	my_dict={'msg':msg}
	return render(request,'seventhapp/display.html',context=my_dict)
	

def balance(request):
	msg='client is checking the Balance amount'
	my_dict={'msg':msg}
	return render(request,'seventhapp/display.html',context=my_dict)
	
def withdraw(request):
	msg='client is withdrawing the Balance amount'
	my_dict={'msg':msg}
	return render(request,'seventhapp/display.html',context=my_dict)
	
