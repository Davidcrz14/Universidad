from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    ANNOUNCEMENT = 'announcement'
    ALERT = 'alert'
    MESSAGE = 'message'

    NOTIFICATION_TYPES = [
        (ANNOUNCEMENT, 'Anuncio'),
        (ALERT, 'Alerta'),
        (MESSAGE, 'Mensaje'),
    ]

    recipients = models.ManyToManyField(User, related_name='notifications')
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.notification_type}: {self.message[:50]}"
