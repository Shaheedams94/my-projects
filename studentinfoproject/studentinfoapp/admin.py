from django.contrib import admin
from .models import student_info

# Register your models here.(request):
class student_infoAdmin(admin.ModelAdmin):
    '''
        Admin View for student-info
    '''
    list_display = ('FIRSTNAME','LASTNAME','CLG','BRANCH','CGPA')
    

admin.site.register(student_info, student_infoAdmin)
