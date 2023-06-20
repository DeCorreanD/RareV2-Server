from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Subscription, User
from rest_framework.decorators import action


class SubscriptionView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
      """Handle GET requests for single song
      
      Returns:
        Response -- JSON serialized song
        """
      try:  
          subscription = Subscription.objects.get(pk=pk)
          
          serializer = SubscriptionSerializer(subscription)
          return Response(serializer.data, status=status.HTTP_200_OK)
        
      except Subscription.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """DOCSTRING
        """
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        user = User.objects.get(id=request.data["follower_id"])
        user = User.objects.get(id=request.data["author_id"])

        subscription = Subscription.objects.create(
            created_on=request.data["created_on"],
            ended_on=request.data["ended_on"],
            follower_id=user,
            author_id=user,
        )
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def destroy(self, request, pk):
        subscription = Subscription.objects.get(pk=pk)
        subscription.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SubscriptionSerializer(serializers.ModelSerializer):
  """JSON serializer for songs"""
  # genres = SongGenreSerializer(many=True, read_only=True)
  
  class Meta:
      model = Subscription
      fields = ('id', 'follower_id', 'author_id', 'created_on', 'ended_on')
      depth = 1
