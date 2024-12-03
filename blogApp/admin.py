from django.contrib import admin
from .models import blogApp
# Register your models here.
class Display_list(admin.ModelAdmin):
    list_display = ('title','desc','img','create_at','update_at')

    
admin.site.register(blogApp,Display_list)