from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer, NotificationDetailSerializer
from rest_framework.permissions import IsAuthenticated
from auth_app.permissions import IsDirectorGlobal, IsDirectorInstituto, IsJefeCarrera, IsProfessor

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filtra las notificaciones para mostrar solo las del usuario actual
        """
        return Notification.objects.filter(recipients=self.request.user)

    def perform_create(self, serializer):
        """
        Al crear una notificación, asegura que el usuario actual sea uno de los destinatarios
        """
        notification = serializer.save()
        notification.recipients.add(self.request.user)

    def get_permissions(self):
        """
        Solo usuarios con roles específicos pueden crear notificaciones
        """
        if self.action == 'create':
            return [IsAuthenticated(), (IsDirectorGlobal() | IsDirectorInstituto() | IsJefeCarrera() | IsProfessor())]
        return [IsAuthenticated()]

    @action(detail=True, methods=['put'])
    def read(self, request, pk=None):
        """
        Marca una notificación como leída
        """
        notification = self.get_object()
        notification.read = True
        notification.save()
        return Response({'status': 'notification marked as read'})

    def get_serializer_class(self):
        """
        Usa un serializer diferente para detalles
        """
        if self.action in ['retrieve', 'read']:
            return NotificationDetailSerializer
        return NotificationSerializer
