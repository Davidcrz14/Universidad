from django.contrib import admin
from .models import Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_type', 'publication_date']
    search_fields = ['title', 'content']
    list_filter = ['publication_type', 'institute']
