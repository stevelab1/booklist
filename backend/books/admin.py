from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_published', 'updated')
    list_display_links = ('id', 'title')
    list_filter = ('author', 'section', 'mood', 'updated', 'featured', 'free_version_available', 'is_published')
    list_editable = ('is_published', )
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 25

admin.site.register(Book, BookAdmin)