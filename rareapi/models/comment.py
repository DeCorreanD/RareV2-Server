from django.db import models
from .post import Post
from .user import User

class Comment(models.Model):

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    created_on = models.DateTimeField(null=True, blank=True)

    @property
    def commenter_name(self):
        '''Custom Property to get the commenter name'''
        return f'{self.author_id.first_name} {self.author_id.last_name}'
