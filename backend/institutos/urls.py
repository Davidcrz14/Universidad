from django.urls import path
from .views import InstituteList, InstituteDetail, InstituteProfessorsViewSet

urlpatterns = [
    path('institutes/', InstituteList.as_view(), name='institute-list'),
    path('institutes/<int:pk>/', InstituteDetail.as_view(), name='institute-detail'),
    path('institutes/<int:institute_id>/professors/', InstituteProfessorsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('professors/<int:id>/', InstituteProfessorsViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('institutes/<int:institute_id>/professors/<int:id>/', InstituteProfessorsViewSet.as_view({'delete': 'destroy'})),
]
