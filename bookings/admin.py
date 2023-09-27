from django.contrib import admin
from . models import Booking
# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','model_name','phone','address','created_date')
    list_display_links=('id','first_name','last_name')
    search_fields=('first_name','last_name','email','model_name')
    list_per_page=25


admin.site.register(Booking,BookingAdmin)