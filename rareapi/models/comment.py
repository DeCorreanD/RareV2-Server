from django.db import models

class Comments(models.Model):

    post_id = models.CharField(max_length=50)
    artist_id = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    created_on = models.DateTimeField(null=True, blank=True)
    