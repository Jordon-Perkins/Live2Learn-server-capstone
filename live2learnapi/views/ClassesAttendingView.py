"""View module for handling requests about classes attending"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from live2learnapi.models import UserProfile, ThisClass, Student, Tag, Skill


class ClassesAttendingView(ViewSet):
    """Live2Learn user view"""

    def list(self, request):
        """Handle GET requests to get all classes
        Returns:
            Response -- JSON serialized list of classes
        """
        # Set the `joined` property on every event
        # for this_class in classes:
        #     # Check to see if the gamer is in the attendees list on the event
        #     this_class.joined = Student in this_class.attendees.all()
        print("Getting all classes")
        classes = ThisClass.objects.filter(student_class__user=request.auth.user)
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ( 'id', 'tag', )

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ( 'id', 'full_name', )

        

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ( 'id','skill_level', )

class ClassesSerializer(serializers.ModelSerializer):
    """JSON serializer for classes
    """
    instructors = StudentSerializer(many=True)
    skill = SkillSerializer(many=False)
    tags = TagSerializer(many=True)

    class Meta:
        model = ThisClass
        fields = ('id', 'title', 'instructors', 'description', 'date', 'time', 'students', 'skill', "tags",
        'joined')