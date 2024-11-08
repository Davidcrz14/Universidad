from rest_framework import viewsets
from .models import File
from .serializers import FileSerializer
from rest_framework.permissions import IsAuthenticated

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated, IsDirectorGlobal | IsDirectorInstituto | IsJefeCarrera | IsProfessor]
        return [IsAuthenticated]
