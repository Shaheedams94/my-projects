from django.shortcuts import render
from datetime import datetime

# Create your views here.
def greeting_dhoni(request):
	date=datetime.now()
	time=int(date.strftime('%H'))
	msg1='thank you so much dhoni... for all wonderfull memories..thank u for making us proud'


	my_dict={'msg1':msg1,'time':time,'date':date}
	return render(request,'fifthapp/fifthapp.html',context=my_dict)