from django.shortcuts import render
from django.db.models.functions import Length
from django.db.models import Q
from app.models import *
# Create your views here.
def display_topics(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render(request,'display_topics.html',d)

def display_webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(topic_name='pubg')
    #webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.all().order_by('-name')
    #webpages=Webpage.objects.all().order_by(Length('name'))
    #webpages=Webpage.objects.all().order_by(Length('name').desc())
    #webpages=Webpage.objects.filter(name__startswith='s')
    #webpages=Webpage.objects.filter(name__endswith='a')
    #webpages=Webpage.objects.filter(name__contains='s')
    #webpages=Webpage.objects.filter(name__regex=r'^[a-zA-Z]{3}a')
    #webpages=Webpage.objects.filter(name__in=('Mary','Sean'))
    webpages=Webpage.objects.filter(Q(topic_name='pubg')&Q(url__startswith='http'))

  
    d={'ws':webpages}
    return render(request,'display_webpage.html',d)


def display_Access(request):
    Access=AccesRecords.objects.all()
    #Access=AccesRecords.objects.all().order_by('date')
    #Access=AccesRecords.objects.filter(date='2000-04-24')
    #Access=AccesRecords.objects.filter(date__year='1975')
    Access=AccesRecords.objects.filter(date__month='10')
    Access=AccesRecords.objects.filter(date__day='24')
    Access=AccesRecords.objects.filter(date__gt='2000-04-24')
    Access=AccesRecords.objects.filter(date__lt='2000-04-24')

    d={'as':Access}
    return render(request,'display_Access.html',d)