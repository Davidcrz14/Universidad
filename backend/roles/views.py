from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from auth_app.permissions import IsAdmin
from .models import Role, UserRole
from .serializers import RoleSerializer, UserRoleSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from auth_app.models import User

User = get_user_model()

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    @action(detail=True, methods=['post'], url_path='assign-user/(?P<user_id>[^/.]+)')
    def assign_user(self, request, pk=None, user_id=None):
        role = self.get_object()
        user = get_object_or_404(User, pk=user_id)

        user_role, created = UserRole.objects.get_or_create(
            user=user,
            role=role,
            defaults={'assigned_by': request.user}
        )

        if created:
            return Response({'message': f'Role {role.name} assigned to user {user.username}'})
        return Response({'message': 'User already has this role'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='remove-user/(?P<user_id>[^/.]+)')
    def remove_user(self, request, pk=None, user_id=None):
        role = self.get_object()
        user = get_object_or_404(User, pk=user_id)

        try:
            user_role = UserRole.objects.get(user=user, role=role)
            user_role.delete()
            return Response({'message': f'Role {role.name} removed from user {user.username}'})
        except UserRole.DoesNotExist:
            return Response({'message': 'User does not have this role'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def list_roles(request):
    roles = [
        {
            'id': role[0],
            'name': role[1]
        }
        for role in User.ROLE_CHOICES
    ]
    return Response(roles)
