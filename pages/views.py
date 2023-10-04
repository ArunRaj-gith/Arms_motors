from django.shortcuts import render
from . models import Team,New,Certificate,Showroom_Video,Bike_Model,Showroom,Award,Inauguration,Event

# Create your views here.
def home(request):
    teams=Team.objects.all()
    news= New.objects.all()
    certificates=Certificate.objects.all()
    videos=Showroom_Video.objects.all()
    bike_info=Bike_Model.objects.all()
    data={
        'teams':teams,
        'news':news,
        'certificates':certificates,
        'videos':videos,
        'bike_info':bike_info,
        }
    return render(request,'pages/home.html',data)


def dealership(request):
    return render(request,'pages/dealership.html')


def gallery(request):
    showrooms=Showroom.objects.all()
    awards=Award.objects.all()
    inaugurations=Inauguration.objects.all()
    events=Event.objects.all()
    data={
        'showrooms':showrooms,
        'awards':awards,
        'inaugurations':inaugurations,
        'events':events,

        }
    return render(request,'pages/gallery.html',data)

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
