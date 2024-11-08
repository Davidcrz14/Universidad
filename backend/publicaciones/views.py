from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Publication
from .serializers import PublicationSerializer, PublicationDetailSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    serializer_class = PublicationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Publication.objects.all()
        publication_type = self.request.query_params.get('type', None)
        institute_id = self.request.query_params.get('institute', None)

        if publication_type is not None:
            queryset = queryset.filter(publication_type=publication_type)
        if institute_id is not None:
            queryset = queryset.filter(institute__id=institute_id)

        return queryset

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return PublicationDetailSerializer
        return PublicationSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
