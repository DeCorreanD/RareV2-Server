from django.db import models

class Subscription(models.Model):
    follower_id = models.CharField(max_length=50)
    author_id = models.CharField(max_length=50)
    created_on = models.CharField(max_length=50)
    ended_on = models.CharField(max_length=50)
