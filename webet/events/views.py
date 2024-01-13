from rest_framework import viewsets

from events.serializers import EventSerializer, MatchSerializer, MatchTeamSerializer
from events.models import Event, Match, MatchTeam

class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class MatchView(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()

    def filter_queryset(self, queryset):
        """
        Filter the queryset to only the matches for the given event ID, if one is provided
        """
        event_id = self.request.query_params.get('event')
        if event_id is not None:
            queryset = queryset.filter(event=event_id)
        return queryset


class MatchTeamView(viewsets.ModelViewSet):
    serializer_class = MatchTeamSerializer
    queryset = MatchTeam.objects.all()

    def filter_queryset(self, queryset):
        """
        Filter the queryset to only the match teams for the given match ID, if one is provided
        """
        match_id = self.request.query_params.get('match')
        if match_id is not None:
            queryset = queryset.filter(match=match_id)
        return queryset
