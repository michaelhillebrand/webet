from rest_framework import serializers
from events.models import Event, Match


class EventSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Event
        fields = ('id', 'name', 'start_time', 'end_time', 'tags')


class MatchSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Match
        fields = ('id', 'name', 'start_time', 'status',
                  'bet_type', 'notes', 'results', 'event', 'tags')
