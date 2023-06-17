from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    profile_image_url = models.URLField()
    email = models.EmailField()
    created_on = models.DateField()
    active = models.BooleanField(null=True, blank=True)
    uid = models.CharField(max_length=10)
