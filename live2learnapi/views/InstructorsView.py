"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from live2learnapi.models import Instructor, UserProfile


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
        instructors = Instructor.objects.all()
        serializer = InstructorSerializer(instructors, many=True)
        return Response(serializer.data)

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserProfile
#         fields = ( 'id', 'bio', )


class InstructorSerializer(serializers.ModelSerializer):
    """JSON serializer for instructors
    """

    # bio = UserSerializer(many=True)

    class Meta:
        model = Instructor
        fields = ('id', 'user_id', 'this_class_id', 'full_name', 'bio',)