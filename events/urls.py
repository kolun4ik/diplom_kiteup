from django.urls import path, re_path
from .views import EventsListView, EventDetailView, EventsYearArchiveView, EventsMonthArchiveView

urlpatterns = [
    path('', EventsListView.as_view(), name='events_view'),
    path('<slug:slug>', EventDetailView.as_view(), name='event'),
    re_path(r'^(?P<year>\d{4})/$', EventsYearArchiveView.as_view(), name='event_year'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d+)/$', EventsMonthArchiveView.as_view(), name='event_month')
]