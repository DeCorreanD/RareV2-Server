from django.db import models

class Comment(models.Model):

    post_id = models.CharField(max_length=50)
    author_id = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    created_on = models.DateTimeField(null=True, blank=True)
    