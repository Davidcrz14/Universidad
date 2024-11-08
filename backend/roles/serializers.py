from rest_framework import serializers
from .models import Role, UserRole
from django.contrib.auth.models import Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename']

class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'permissions', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id', 'user', 'role', 'assigned_at', 'assigned_by']
        read_only_fields = ['assigned_at', 'assigned_by']
