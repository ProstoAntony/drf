from . models import Game
from rest_framework import serializers

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__')