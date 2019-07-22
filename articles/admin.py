from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Article

# Register your models here.
class ArticleAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','published','status')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article, ArticleAdmin)