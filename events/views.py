from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Event


class EventsListView(ListView):
    template_name = 'events/all_events.html'
    context_object_name = 'list_events'

    def get_queryset(self):
        return Event.objects.all()


class EventDetailView(DetailView):
    template_name = "events/event.html"
    model = Event
    context_object_name = 'event'


