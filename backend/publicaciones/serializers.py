from rest_framework import serializers
from .models import Publication

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'title', 'content', 'publication_date', 'author', 'publication_type', 'institute']

    def validate_title(self, value):
        if len(value) > 255:
            raise serializers.ValidationError("El título no puede tener más de 255 caracteres.")
        return value

class PublicationDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    institute = serializers.StringRelatedField()

    class Meta:
        model = Publication
        fields = ['id', 'title', 'content', 'publication_date', 'author', 'publication_type', 'institute']
