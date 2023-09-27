from django.shortcuts import redirect, render
from . models import Booking
from django.contrib import messages

# Create your views here.
def bookings(request):
    
    if request.method == 'POST': 
        country =request.POST['country']
        district =request.POST['district']
        state =request.POST['state']
        model_name= request.POST['model_name']
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        email =request.POST['email']
        phone =request.POST['phone']
        address =request.POST['address']
        description =request.POST['description']
        
        
        booking=Booking(country=country,district=district,state=state,model_name=model_name,first_name=first_name,last_name=last_name,
                        email=email,phone=phone,address=address,description=description)
        booking.save()
        messages.success(request,'Your request has been submitted,we will get back to you shortly')
    
    return redirect('bookingform')