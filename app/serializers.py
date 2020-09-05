from rest_framework import serializers
from .models import League, Team

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id','name','photo_url']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'league','preview_url']