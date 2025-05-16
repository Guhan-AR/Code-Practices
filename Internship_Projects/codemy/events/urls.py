from django.urls import path
from . import views

urlpatterns = [
    path('events/',views.all_events,name='list-events'),
    path('<int:year>/<str:month>',views.calendar),
    path('<str:name>/<int:year>/<str:month>',views.calendar),
    path('',views.calendar,name='calendar'),
    path('add_venue/',views.add_venue,name='add-venue'),
    path('list_venue/',views.list_venue,name='list-venue'),
    path('venue/<venue_id>',views.venue,name='venue'),
    path('search_venues',views.venue_search,name='venue-search'),
    path('update_venue/<int:venue_id>',views.update_venue,name='update-venue'),
    path('update_event/<int:event_id>',views.update_event,name='update-event'),
    path('add_event/',views.add_event,name='add-event'),
    path('delete_venue/<int:id>',views.delete_venue,name='delete-venue'),
    path('delete_event/<int:id>',views.delete_event,name='delete-event'),
]