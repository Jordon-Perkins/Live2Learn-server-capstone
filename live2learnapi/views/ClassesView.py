"""View module for handling requests about class"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from live2learnapi.models import ThisClass, Instructor, UserProfile, Skill, Tag, Student
from rest_framework.decorators import action

class ClassesView(ViewSet):
    """ive2Learn classes view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single class
        Returns:
            Response -- JSON serialized event
        """
        this_class = ThisClass.objects.get(pk=pk)
        serializer = ClassesSerializer(this_class)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all classes
        Returns:
            Response -- JSON serialized list of classes
        """
        # Set the `joined` property on every event
        # for this_class in classes:
        #     # Check to see if the gamer is in the attendees list on the event
        #     this_class.joined = Student in this_class.attendees.all()

        classes = ThisClass.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations 
        Returns
            Response -- JSON serialized class instance
        """
        # instructor = Instructor.objects.get(user=request.auth.user)
        # student = Student.objects.get(user=request.auth.user)
        skill = Skill.objects.get(pk=request.data["skillId"])

        this_class = ThisClass.objects.create(
            date=request.data["date"],
            time=request.data["time"],
            title=request.data["title"],
            description=request.data["description"],
            # instructor=instructor,
            # students=student,
            skill=skill
        )

        Instructor.objects.create(
            user=request.auth.user, this_class=this_class
        )

        serializer = ClassesSerializer(this_class)
        return Response(serializer.data)


    def update(self, request, pk):
        """Handle PUT requests for a class
        Returns:
            Response -- Empty body with 204 status code
        """

        this_class = ThisClass.objects.get(pk=pk)
        this_class.date = request.data["date"]
        this_class.time = request.data["time"]
        this_class.description = request.data["description"]
        this_class.title = request.data["title"]
    
        skill = Skill.objects.get(pk=request.data["skillId"])
        this_class.skill = skill
        this_class.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


    def destroy(self, request, pk):
        this_class = ThisClass.objects.get(pk=pk)
        this_class.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        """Post request for a user to sign up for an event"""
    
        student = UserProfile.objects.get(user=request.auth.user)
        this_class = ThisClass.objects.get(pk=pk)
        this_class.ThisClass.add(student)
        return Response({'message': 'student was added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        """Delete request for a user to sign up for an event"""
    
        student = UserProfile.objects.get(user=request.auth.user)
        this_class = ThisClass.objects.get(pk=pk)
        Student.objects.get(student=student, this_class=this_class).delete()
        return Response({'message': 'this student was removed'}, status=status.HTTP_204_NO_CONTENT)

class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructor
        fields = ( 'id', 'full_name', )

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ( 'id','skill_level', )

class ClassesSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    instructors = InstructorSerializer(many=True)
    skill = SkillSerializer(many=False)

    class Meta:
        model = ThisClass
        fields = ('id', 'title', 'instructors', 'description', 'date', 'time', 'students', 'skill',
        'joined')