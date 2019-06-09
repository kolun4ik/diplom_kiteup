from django.contrib import admin
from .models import ItemNews

# Register your models here.

class AdminNews(admin.ModelAdmin):
    list_display = ('title_news', 'creation_date')
    ordering = ('creation_date',)
    search_fields = ('title_news',)

admin.site.register(ItemNews, AdminNews)
