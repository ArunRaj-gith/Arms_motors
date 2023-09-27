from django.contrib import admin
from . models import Dealership
# Register your models here.
class DealershipAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','source','phone','address','created_date')
    list_display_links=('id','first_name','last_name')
    search_fields=('first_name','last_name','email','source','investment')
    list_per_page=25



admin.site.register(Dealership,DealershipAdmin)