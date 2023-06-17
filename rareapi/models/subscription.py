from django.db import models
from .user import User

class Subscription(models.Model):
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower_id")
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_id")
    created_on = models.DateField()
    ended_on = models.DateField()
