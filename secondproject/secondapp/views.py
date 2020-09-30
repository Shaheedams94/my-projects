from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def greeting_django(request):
	s1='<center><h1>Hello..Good marning!!</h1></center>'
	time=datetime.now().time()
	greeting=s1+'<center><h1>The server time is:'+str(time)+'</h1></center>'

	return HttpResponse(greeting)
