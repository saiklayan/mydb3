from django.shortcuts import render
from django.db.models.functions import Length
from app.models import *
# Create your views here.
def display_topics(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render(request,'display_topics.html',d)

def display_webpage(request):
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(topic_name='pubg')
    webpages=Webpage.objects.all().order_by('name')
    webpages=Webpage.objects.all().order_by('-name')
    webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.all().order_by(Length('name').desc())
    d={'ws':webpages}
    return render(request,'display_webpage.html',d)


def display_Access(request):
    Access=AccesRecords.objects.all()
    Access=AccesRecords.objects.all().order_by('date')
    d={'as':Access}
    return render(request,'display_Access.html',d)