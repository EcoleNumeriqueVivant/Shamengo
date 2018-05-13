from django.contrib import admin

from scheduler.models import Category, Entry

admin.site.register(Entry)
admin.site.register(Category)
