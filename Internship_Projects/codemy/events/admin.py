from django.contrib import admin
from . import models

# admin.site.register(models.Venue_DB)
# admin.site.register(models.TurfUsers_DB)
# admin.site.register(models.Event_DB)

@admin.register(models.Venue_DB)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone')
    ordering = ('name',)
    search_fields = ('name','address')

@admin.register(models.TurfUsers_DB)
class TurfAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    ordering = ('first_name',)
    search_fields = ('first_name',)

@admin.register(models.Event_DB)
class EventAdmin(admin.ModelAdmin):
    fields = (('name','venue'),'date','manager','description')
    list_display = ('name','date','venue')
    list_filter = ('date','venue')
    ordering = ('-name',)