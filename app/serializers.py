from rest_framework import serializers
from .models import League, Team, Federation, Tournament, Championship

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


class  TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['name', 'photo_url']


class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = ['name', 'photo_url']