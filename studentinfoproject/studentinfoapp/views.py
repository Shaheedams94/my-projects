from django.shortcuts import render
from .models import student_info

# Create your views here.
def display(request):
	stud_list=student_info.objects.all()

	my_dict={'student':stud_list}
	return render(request,'studentinfoapp/studentinfo.html',{'student':stud_list})
