from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, User, Comment
from datetime import datetime

class CommentView(ViewSet):
    """Rare comments view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single comment
        Returns:
            Response -- JSON serialized comment
        """
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all comments

        Returns:
            Response -- JSON serialized list of comments
        """
        post_id = request.query_params.get('postId', None)
        comment = Comment.objects.all().filter(post_id=post_id)

        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized comment instance
        """
        post_id = Post.objects.get(pk=request.data["postId"])
        author_id = User.objects.get(pk=request.data["authorId"])

        comment = Comment.objects.create(
            author_id=author_id,
            post_id=post_id,
            content=request.data["content"],
            created_on=datetime.now(),
        )

        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a comment
        
        Returns -- Empty body with 204 status code
        """

        comment = Comment.objects.get(pk=pk)
        comment.content = request.data["content"]
        # comment.created_on = request.data["created_on"]

        # author_id = User.objects.get(pk=request.data["authorId"])
        # comment.author_id = author_id

        # post_id = Post.objects.get(pk=request.data["postId"])
        # comment.post_id = post_id

        comment.save()

        return Response(None, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        """Delete Comments
        """
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class  CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments
    """
    created_on = serializers.DateTimeField(format="%B %d, %Y, %I:%M%p")
    class Meta:
        model = Comment
        fields = ('id', 'author_id', 'post_id', 'content', 'created_on', 'commenter_name')
        depth = 1
