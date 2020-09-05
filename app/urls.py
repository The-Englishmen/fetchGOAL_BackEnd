from django.urls import path 
from . import views 
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('league/', views.LeagueList.as_view(), name='league_list'),
]