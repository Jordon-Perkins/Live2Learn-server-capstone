"""View module for handling requests about skills"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from live2learnapi.models import Skill


class SkillView(ViewSet):
    """Live2Learn skill view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single skill level
        Returns:
            Response -- JSON serialized skill
        """
        skill_level = Skill.objects.get(pk=pk)
        serializer = SkillSerializer(skill_level)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all skill levels
        Returns:
            Response -- JSON serialized list of skill levels
        """
        skill_levels = Skill.objects.all()
        serializer = SkillSerializer(skill_levels, many=True)
        return Response(serializer.data)



class SkillSerializer(serializers.ModelSerializer):
    """JSON serializer for skill level
    """
    class Meta:
        model = Skill
        fields = ('id', 'skill_level')