from rest_framework import generics
from .serializers import LeagueSerializer, TeamSerializer, FederationSerializer, TournamentSerializer
from .models import League, Team, Federation, Tournament

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

class TournamentList(generics.ListCreateAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TournamentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer