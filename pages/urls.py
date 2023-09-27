from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dealership',views.dealership,name='dealership'),
    path('gallery',views.gallery,name='gallery'),
    path('contact',views.contact,name='contact'),
    path('ebikes',views.ebikes,name='ebikes'),
    path('bookingform',views.bookingform,name='bookingform'),
    
    
    # path('select_color',views.select_color,name='select_color'),
    
    
]