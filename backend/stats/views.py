from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from auth_app.permissions import IsAdmin, IsDirectorGlobal, IsDirectorInstituto
from auth_app.models import User
from publicaciones.models import Publication
from notificaciones.models import Notification
from institutos.models import Institute

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin | IsDirectorGlobal | IsDirectorInstituto])
def general_stats(request):
    """Obtener estadísticas generales de la plataforma"""
    stats = {
        'total_users': User.objects.count(),
        'total_publications': Publication.objects.count(),
        'total_notifications': Notification.objects.count(),
        'total_institutes': Institute.objects.count(),
    }
    return Response(stats)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin | IsDirectorGlobal | IsDirectorInstituto])
def publication_stats(request):
    """Estadísticas sobre publicaciones"""
    stats = {
        'by_type': Publication.objects.values('publication_type').annotate(count=Count('id')),
        'by_institute': Publication.objects.values('institute__name').annotate(count=Count('id')),
        'recent_publications': Publication.objects.order_by('-publication_date')[:5].values('title', 'publication_date'),
    }
    return Response(stats)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin | IsDirectorGlobal | IsDirectorInstituto])
def notification_stats(request):
    """Estadísticas de notificaciones"""
    stats = {
        'total_sent': Notification.objects.count(),
        'total_read': Notification.objects.filter(read=True).count(),
        'total_unread': Notification.objects.filter(read=False).count(),
        'by_type': Notification.objects.values('notification_type').annotate(count=Count('id')),
    }
    return Response(stats)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin | IsDirectorGlobal | IsDirectorInstituto])
def user_stats(request):
    """Estadísticas de usuarios"""
    stats = {
        'by_role': User.objects.values('role').annotate(count=Count('id')),
        'by_institute': User.objects.values('institute__name').annotate(count=Count('id')),
        'active_users': User.objects.filter(is_active=True).count(),
        'inactive_users': User.objects.filter(is_active=False).count(),
    }
    return Response(stats)
