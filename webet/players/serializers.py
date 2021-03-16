from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name', 'prefix', 'suffix', 'version', 'tags')
