from django.db import models
from django.contrib.auth.models import AbstractUser
from institutos.models import Institute

class User(AbstractUser):
    ADMIN = 'admin'
    DIRECTOR_GLOBAL = 'director_global'
    DIRECTOR_INSTITUTO = 'director_instituto'
    JEFE_CARRERA = 'jefe_carrera'
    PROFESSOR = 'professor'
    STUDENT = 'student'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (DIRECTOR_GLOBAL, 'Director Global'),
        (DIRECTOR_INSTITUTO, 'Director de Instituto'),
        (JEFE_CARRERA, 'Jefe de Carrera'),
        (PROFESSOR, 'Profesor'),
        (STUDENT, 'Estudiante'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
