from django.shortcuts import redirect, render
from django.contrib import messages
from . models import Contact


# Create your views here.
def enquiry(request):
    if request.method == 'POST': 
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        customer_need =request.POST['customer_need']
        email =request.POST['email']
        phone =request.POST['phone']
        address =request.POST['address']
        message =request.POST['message']
        
        
        contact=Contact(first_name=first_name,last_name=last_name,customer_need=customer_need,
                        email=email,phone=phone,address=address,message=message)
        contact.save()
        messages.success(request,'Your request has been submitted,we will get back to you shortly')
        return redirect('contact')
    
