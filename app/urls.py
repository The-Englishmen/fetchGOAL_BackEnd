from django.urls import path 
from . import views 
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('league/', views.LeagueList.as_view(), name='league_list'),
    path('team/', views.TeamList.as_view(), name='team_list'),
    path('federation/', views.FederationList.as_view(), name='federation_list'),
    path('tournament/', views.TournamentList.as_view(), name='tournament_list'),
    path('championship/', views.ChampionshipList.as_view(), name='championship_list'),
    
]