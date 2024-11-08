from django.db import models
from django.conf import settings

class Institute(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='institute_logos/', null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    director = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='directed_institute'
    )
    established_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Career(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    career = models.ForeignKey(Career, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
