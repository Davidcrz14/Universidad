from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'description', 'file', 'owner', 'institute', 'career', 'subject', 'created_at', 'updated_at']
        read_only_fields = ['owner', 'created_at', 'updated_at']
