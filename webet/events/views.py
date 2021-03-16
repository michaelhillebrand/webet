from rest_framework import viewsets

from events.serializers import EventSerializer
from events.models import Event

class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
