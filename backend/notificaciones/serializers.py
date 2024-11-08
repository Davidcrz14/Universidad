from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipients', 'message', 'notification_type', 'created_at', 'read']
        read_only_fields = ['created_at']

    def validate_message(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("El mensaje no puede tener más de 500 caracteres.")
        return value

class NotificationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipients', 'message', 'notification_type', 'created_at', 'read']
        read_only_fields = ['created_at', 'recipients', 'message', 'notification_type']
