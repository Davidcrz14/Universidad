from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Publication
from institutos.models import Institute
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'universidad_virtual.settings')
django.setup()

User = get_user_model()

class PublicationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.institute = Institute.objects.create(name='Test Institute')
        self.publication = Publication.objects.create(
            title='Test Publication',
            content='Test content',
            author=self.user,
            publication_type=Publication.ANNOUNCEMENT,
            institute=self.institute
        )

    def test_get_publications(self):
        """
        Prueba para obtener todas las publicaciones
        """
        url = reverse('publication-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_publication_detail(self):
        """
        Prueba para obtener los detalles de una publicación
        """
        url = reverse('publication-detail', args=[self.publication.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_publication(self):
        """
        Prueba para crear una nueva publicación
        """
        self.client.login(username='testuser', password='testpass')
        url = reverse('publication-list')
        data = {
            'title': 'New Publication',
            'content': 'New content',
            'publication_type': Publication.NEWS,
            'institute': self.institute.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_publication(self):
        """
        Prueba para actualizar una publicación existente
        """
        self.client.login(username='testuser', password='testpass')
        url = reverse('publication-detail', args=[self.publication.id])
        data = {
            'title': 'Updated Publication',
            'content': 'Updated content'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_publication(self):
        """
        Prueba para eliminar una publicación
        """
        self.client.login(username='testuser', password='testpass')
        url = reverse('publication-detail', args=[self.publication.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
