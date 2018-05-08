from django.shortcuts import render
from scheduler.models import Entry

def index(request):
    entries = Entry.objects.all()
    return render(request,'scheduler.html', {'entries': entries})

def details(request, pk):
    return render (request, 'details.html')
