from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, User

class PostView(ViewSet):
    """RareAPI Post View"""
    
    def retrieve(self, request, pk):
      
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def list(self, request):

        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    def create(self, request):

        rare_user_id = User.objects.get(uid=request.data["rare_user_id"])
        
        post = Post.objects.create(
        title=request.data["title"],
        publication_date=request.data["publication_date"],
        image_url=request.data["image_url"],
        content=request.data     ["content"],  
        rare_user_id=rare_user_id
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)
      
    def update(self, request, pk):
        """ PUT Request For Post
        Returns:
        Response -- Empty Body With 204 Status Code
        """
        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.publication_date = request.data["publication_date"]
        post.image_url = request.data["image_url"]
        post.content = request.data["content"]
        
        rare_user_id = User.objects.get(pk=request.data["rare_user_id"])
        post.rare_user_id = rare_user_id
        post.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    def destroy( self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
class PostSerializer(serializers.ModelSerializer):
    """JSON Serializer For Post
    """
    class Meta:
        model = Post
        fields = ('id', 'rare_user_id', 'title', 'publication_date', 'image_url', 'content' )
    depth = 1
