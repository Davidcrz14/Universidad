from django.urls import path
from . import views

urlpatterns = [
    path('stats/', views.general_stats, name='general-stats'),
    path('stats/publications/', views.publication_stats, name='publication-stats'),
    path('stats/notifications/', views.notification_stats, name='notification-stats'),
    path('stats/users/', views.user_stats, name='user-stats'),
]
