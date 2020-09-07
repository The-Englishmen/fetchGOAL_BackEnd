from rest_framework import generics
from .serializers import LeagueSerializer, TeamSerializer, FederationSerializer
from .models import League, Team, Federation

# Create your views here.

class LeagueList(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class LeagueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class FederationList(generics.ListCreateAPIView):
    queryset = Federation.objects.all()
    serializer_class = FederationSerializer


class FederationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Federation.objects.all()
    serializer_class = FederationSerializer