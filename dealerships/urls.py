from django.urls import path
from . import views

urlpatterns = [
    path('dealerships',views.dealerships,name='dealerships'),
]