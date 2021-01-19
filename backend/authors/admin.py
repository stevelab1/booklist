from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updated')
    list_display_links = ('id', 'name')
    list_filter = ('updated', 'featured')
    search_fields = ('name', 'description')
    list_per_page = 25

admin.site.register(Author, AuthorAdmin)


