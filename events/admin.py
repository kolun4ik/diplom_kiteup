from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Event

# Register your models here.
class EventAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('title','slug','published','visible')
    fields = ('slug','title','longtitle','description','introtext','content','image','published','visible')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Event, EventAdmin)