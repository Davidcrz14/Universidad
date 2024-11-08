from django.contrib import admin
from .models import Institute, Career, Subject

@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ['name', 'director', 'active']
    search_fields = ['name', 'description']
    list_filter = ['active']

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['name', 'institute']
    search_fields = ['name', 'description']
    list_filter = ['institute']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'career']
    search_fields = ['name', 'description']
    list_filter = ['career']
