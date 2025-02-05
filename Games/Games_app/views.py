import django_filters.rest_framework

from . models import Game
from rest_framework import generics
from .serializers import GamesSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from . permissions import AllForAdminOtherReadOnly
from rest_framework import filters





class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GamesSerializer
    permission_classes = (AllForAdminOtherReadOnly,)
    filter_backends = [filters.OrderingFilter]
    search_fields = ['name', 'developers_company', 'description', 'mark',  'price_usd']



