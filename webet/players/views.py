from rest_framework import viewsets

from players.serializers import PlayerSerializer
from players.models import Player


class PlayerView(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
