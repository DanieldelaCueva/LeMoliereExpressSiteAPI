from django.contrib import admin
from .models import Article, Edition

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author', 'group', 'language']
    list_display = ['title', 'author', 'group', 'language']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Edition)