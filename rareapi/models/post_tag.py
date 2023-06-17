from django.db import models

class PostTag(models.Model):

    post_id = models.CharField(max_length=50)
    tag_id = models.CharField(max_length=50)
