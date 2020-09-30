from django.contrib import admin
from .models import trainer_info

# Register your models here.

class trainer_infoAdmin(admin.ModelAdmin):
    '''
        Admin View for trainer_info
    '''
    list_display = ('FIRSTNAME','LASTNAME','DOMAIN','BRANCH','ADDRESS','EXPERIENCE','SALARY')
    

admin.site.register(trainer_info, trainer_infoAdmin)