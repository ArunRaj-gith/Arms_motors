from django.shortcuts import redirect, render
from . models import Dealership
from django.contrib import messages

# Create your views here.
def dealerships(request):
    
    if request.method == 'POST': 
        country =request.POST['country']
        district =request.POST['district']
        state =request.POST['state']
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        email =request.POST['email']
        phone =request.POST['phone']
        address =request.POST['address']
        description =request.POST['description']
        source =request.POST['source']
        business_experience =request.POST['business_experience']
        investment =request.POST['investment']
        
        
        
        dealership=Dealership(country=country,district=district,state=state,first_name=first_name,last_name=last_name,
                        email=email,phone=phone,address=address,description=description,source=source,
                        business_experience=business_experience,investment=investment)
        
        dealership.save()
        messages.success(request,'Your request has been submitted,we will get back to you shortly')
    
    
    
    return redirect('dealership')