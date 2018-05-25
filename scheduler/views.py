from django.shortcuts import render
from scheduler.models import Entry, Category

# def index(request):
#     entries = Entry.objects.all()
#     return render(request,'index.html', {'entries': entries})

def calender(request):
    entries = Entry.objects.all().order_by('date')
    if not entries :
        return render(request,'no_event.html', {'entries': entries})
    else :
        return render(request,'calender.html', {'entries': entries})

def details(request, pk):
    entry = Entry.objects.get(id=pk)
    return render (request, 'details.html', {'entry': entry})
