from rest_framework import serializers
from .models import League, Team, Federation

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['id','name','photo_url']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name','league','photo_url']


class FederationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Federation
        fields = ['name', 'photo_url']