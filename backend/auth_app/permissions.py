from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsDirectorInstituto(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'director_instituto'

class IsDirectorGlobal(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'director_global'

class IsJefeCarrera(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'jefe_carrera'

class IsProfessor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'professor'
