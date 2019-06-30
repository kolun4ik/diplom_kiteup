from django.contrib import admin
from .models import New

# Register your models here.

class AdminNews(admin.ModelAdmin):
    list_display = ('title', 'created')
    ordering = ('created',)
    search_fields = ('title',)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

admin.site.register(New, AdminNews)
