from rest_framework import serializers
from .models import Institute
from auth_app.models import User
from django.core.exceptions import ValidationError

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ['id', 'name', 'description', 'logo', 'website', 'address', 'phone', 'email', 'director', 'established_date', 'active']

    # Validaciones adicionales
    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError("El nombre del instituto debe tener al menos 3 caracteres.")
        return value

    def validate_website(self, value):
        if value and not value.startswith("http"):
            raise ValidationError("El sitio web debe comenzar con 'http' o 'https'.")
        return value

class InstituteDetailSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField()

    class Meta:
        model = Institute
        fields = ['id', 'name', 'description', 'logo', 'website', 'address', 'phone', 'email', 'director', 'established_date', 'active']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'institute']
        read_only_fields = ['username']

    def validate(self, data):
        if self.instance is None and data.get('role') != User.PROFESSOR:
            raise serializers.ValidationError("El usuario debe tener el rol de profesor")
        return data
