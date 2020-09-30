from django.shortcuts import render
from datetime import datetime

# Create your views here.
def greet_django(request):
	date=datetime.now()
	time=int(date.strftime('%H'))

	if time<12:
		msg='good morning!!'
	elif time<16:
		msg='good afternoon!!'
	elif time<20:
		msg='good evening!!'
	else:
		msg='good night!!'

	my_dict={'my_date':date,'my_msg':msg}
	return render(request,'thirdapp/display.html',context=my_dict)
	#return render(request,'thirdapp/display.html',context=my_dict)

	
	
		

	