from django.db import models
from django.conf import settings
from django.db.models.signals import pre_init, post_save


class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.URLField(max_length=500)
    description = models.TextField()
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)
    interests = models.TextField()

    def __str__(self):
        return self.name
