from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Institute
from auth_app.models import User
from .serializers import InstituteSerializer, InstituteDetailSerializer, ProfessorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from auth_app.permissions import IsAdmin, IsDirectorInstituto

class InstituteList(generics.ListCreateAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(director=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [AllowAny()]

class InstituteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institute.objects.all()
    serializer_class = InstituteDetailSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [AllowAny()]
        return [AllowAny()]

class InstituteProfessorsViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request, institute_id=None):
        professors = User.objects.filter(institute_id=institute_id, role=User.PROFESSOR)
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id=None):
        """Obtener detalles de un profesor específico"""
        professor = get_object_or_404(User, id=id, role=User.PROFESSOR)
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)

    def update(self, request, id=None):
        """Actualizar perfil de un profesor"""
        professor = get_object_or_404(User, id=id, role=User.PROFESSOR)
        serializer = ProfessorSerializer(professor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, institute_id=None):
        """Asignar un profesor a un instituto"""
        institute = get_object_or_404(Institute, id=institute_id)
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(institute=institute, role=User.PROFESSOR)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, institute_id=None, id=None):
        """Remover un profesor de un instituto"""
        professor = get_object_or_404(User, id=id, institute_id=institute_id, role=User.PROFESSOR)
        professor.institute = None
        professor.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        """Verificar permisos según la acción"""
        if self.action in ['create', 'update', 'destroy']:
            return [AllowAny()]
        return [AllowAny()]
