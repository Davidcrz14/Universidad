from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.list_roles, name='list_roles'),
]
