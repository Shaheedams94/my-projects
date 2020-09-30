from django.contrib import admin
from .models import movie_info

# Register your models here.

class movie_infoAdmin(admin.ModelAdmin):
    '''
        Admin View for trainer_info
    '''
    list_display = ('HERO_NAME','HEROINE_NAME','MOVIE_NAME','RELEASE_DATE','MOVIE_DURATION','NO_OF_SONGS')
    

admin.site.register(movie_info, movie_infoAdmin)