from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','slug','visible')
    fields = ('slug','title','description','content','image','published','visible')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Event, EventAdmin)