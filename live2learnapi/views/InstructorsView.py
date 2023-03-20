"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from live2learnapi.models import Instructor, UserProfile
from django.db.models import Count
from rest_framework import serializers


class InstructorsView(ViewSet):
    """Live2Learn instructors view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single instructor
        Returns:
            Response -- JSON serialized instructor
        """
        instructor = Instructor.objects.get(pk=pk)
        serializer = InstructorSerializer(instructor)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all instructors
        Returns:
            Response -- JSON serialized list of instructors
        """
        instructors = (
            UserProfile.objects
            .annotate(n_classes_taught=Count('instructor__this_class_id'))
            .filter(n_classes_taught__gt=0)
            .all()
        )
        serializer = UserProfileSerializer(instructors, many=True)
        return Response(serializer.data)

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserProfile
#         fields = ( 'id', 'bio', )



class UserProfileSerializer(serializers.ModelSerializer):
    """Your data serializer, define your fields here."""
    class Meta:
        model = UserProfile
        fields = ('id', 'full_name', 'bio',)


class InstructorSerializer(serializers.ModelSerializer):
    """JSON serializer for instructors
    """

    class Meta:
        model = Instructor
        fields = ('id', 'user_id', 'this_class_id', 'full_name', 'bio',)