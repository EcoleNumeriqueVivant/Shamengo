from django.shortcuts import render
from scheduler.models import Entry, Category
import datetime 


def calender(request):
    entries = Entry.objects.all().order_by('date_start').exclude(date_end__lt=datetime.datetime.now())
    return render(request,'calender.html', {'entries': entries})

def details(request, pk):
    entry = Entry.objects.get(id=pk)
    return render (request, 'details.html', {'entry': entry})
