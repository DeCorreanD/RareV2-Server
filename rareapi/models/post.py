from django.db import models
from .user import User

class Post(models.Model):
    rare_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.URLField()
    content = models.CharField(max_length=50)
