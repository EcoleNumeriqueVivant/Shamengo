from django.contrib import admin
from scheduler.models import Category, Entry, Theme


def make_published(models, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Publier evenement"

def make_Offline(models, request, queryset):
    queryset.update(status='o')
make_Offline.short_description = "Retirer evenement"

def make_Draft(models, request, queryset):
    queryset.update(status='d')
make_Draft.short_description = "Revenir au brouillon"

class EntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    ordering = ['name']
    actions = [make_published, make_Offline, make_Draft]



admin.site.register(Entry, EntryAdmin)
admin.site.register(Category)
admin.site.register(Theme)
