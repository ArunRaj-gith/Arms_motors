from django.shortcuts import render
from . models import Team,New,Award,Showroom_Video,Bike_Model

# Create your views here.
def home(request):
    teams=Team.objects.all()
    news= New.objects.all()
    awards=Award.objects.all()
    videos=Showroom_Video.objects.all()
    bike_info=Bike_Model.objects.all()
    data={
        'teams':teams,
        'news':news,
        'awards':awards,
        'videos':videos,
        'bike_info':bike_info,
        }
    return render(request,'pages/home.html',data)


def dealership(request):
    return render(request,'pages/dealership.html')


def gallery(request):
    return render(request,'pages/gallery.html')

def contact(request):
    return render(request,'pages/contact.html')

def ebikes(request):
    bike_info=Bike_Model.objects.all()
    data={
        'bike_info':bike_info,
        }
    return render(request,'pages/ebikes.html',data)


def bookingform(request):
    bike_info=Bike_Model.objects.all()
    data={
        'bike_info':bike_info,
        }
    return render(request,'pages/bookingform.html',data)
