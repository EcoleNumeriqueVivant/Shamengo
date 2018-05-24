from django.contrib import admin

from scheduler.models import Category, Entry, Theme

admin.site.register(Entry)
admin.site.register(Category)
admin.site.register(Theme)
