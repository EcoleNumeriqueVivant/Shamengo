from django.shortcuts import render
from .models import Entry


def index(request):
	entries = Entry.objects.all()
	return render(request, 'calender/index.html', {'entries': entries})
