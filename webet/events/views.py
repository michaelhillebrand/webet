from rest_framework import viewsets

from events.serializers import EventSerializer, MatchSerializer
from events.models import Event, Match

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
