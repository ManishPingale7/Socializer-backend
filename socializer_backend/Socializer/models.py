from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    description = models.TextField()
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)
    interests = models.TextField()

    def __str__(self):
        return self.name
