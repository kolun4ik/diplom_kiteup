from django.urls import path, re_path
from .views import EventsListView, EventDetailView

urlpatterns = [
    path('', EventsListView.as_view(), name='events_view'),
    path('<slug:slug>', EventDetailView.as_view(), name='event')
]