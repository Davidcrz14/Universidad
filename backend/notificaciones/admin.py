from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_type', 'created_at', 'read']
    search_fields = ['message']
    list_filter = ['notification_type', 'read']
