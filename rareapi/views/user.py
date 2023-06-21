"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import User
from django.db.models import Count

class UserView(ViewSet):
    """Users view"""
    
    def list(self, request):
        """Handle GET requests to get all users
        Returns:
            Response -- JSON serialized list of users
        """
        user = User.objects.annotate(subscription_count=Count('follower')).all()
        serializer = UserSerializer(user, many=True, context={'request': request})
        return Response(serializer.data)
      
    def retrieve(self, request, pk):
      try:
        user = User.objects.annotate(subscription_count=Count('follower')).get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
      except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        """POST request to create a rare user"""
        uid = request.META["HTTP_AUTHORIZATION"]
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(uid=uid)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
         
    def update(self, request, pk):
        user = User.objects.get(pk=pk)
        uid = request.META["HTTP_AUTHORIZATION"]
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.bio = request.data["bio"]
        user.profile_image_url=request.data["profile_image_url"]
        user.created_on = request.data["created_on"]
        user.email=request.data["email"]
        user.uid = uid
        
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
     
    def destroy(self, request, pk):
        """DELETE request to destroy a rare user"""
        rare_user = User.objects.get(pk=pk)
        rare_user.delete()
        return Response({'message': 'User Destroyed'}, status=status.HTTP_204_NO_CONTENT) 
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for rare users"""
    subscription_count = serializers.IntegerField(default=None)
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'bio',
                  'profile_image_url',
                  'email',
                  'created_on',
                  'active',
                  'subscription_count',
                  'uid')

class CreateUserSerializer(serializers.ModelSerializer):
    """JSON serializer for creating rare users"""
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'bio',
                  'profile_image_url',
                  'email',
                  'active')