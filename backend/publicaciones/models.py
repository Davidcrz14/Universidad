from django.db import models
from django.contrib.auth import get_user_model
from institutos.models import Institute

User = get_user_model()

class Publication(models.Model):
    ANNOUNCEMENT = 'announcement'
    NEWS = 'news'
    EVENT = 'event'

    PUBLICATION_TYPES = [
        (ANNOUNCEMENT, 'Anuncio'),
        (NEWS, 'Noticia'),
        (EVENT, 'Evento'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_type = models.CharField(max_length=20, choices=PUBLICATION_TYPES)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
