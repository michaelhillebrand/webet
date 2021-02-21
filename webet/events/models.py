from django.contrib.auth.models import User
from django.db import models

from base.models import BaseModel
from players.models import Player, Team
from tags.models import Tag


class Event(BaseModel):
    name = models.CharField(max_length=128, blank=False, null=False)
    start_time = models.DateTimeField(blank=False, null=False)
    end_time = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class EventPlayer(BaseModel):
    event = models.ForeignKey(Event, blank=False, null=False, on_delete=models.RESTRICT)
    player = models.ForeignKey(Player, blank=False, null=False, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.event} - {self.player}"


class EventTeam(BaseModel):
    event = models.ForeignKey(Event, blank=False, null=False, on_delete=models.RESTRICT)
    name = models.CharField(max_length=128, blank=False, null=False)
    members = models.ManyToManyField(
        EventPlayer,
        through='EventTeamMembership',
        through_fields=('team', 'player'),
    )

    def __str__(self):
        return f"{self.event} - {self.name}"


class EventTeamMembership(BaseModel):
    team = models.ForeignKey(EventTeam, blank=False, null=False, on_delete=models.RESTRICT)
    player = models.ForeignKey(EventPlayer, blank=False, null=False, on_delete=models.RESTRICT)
    position = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.team.event} - {self.player}"


class EventUser(BaseModel):
    event = models.ForeignKey(Event, blank=False, null=False, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.RESTRICT)
    bucks = models.IntegerField(blank=False, null=False, default=1000)

    def __str__(self):
        return f"{self.event} - {self.user}"


class Match(BaseModel):
    OPEN = 'open'
    STATUSES = (
        (OPEN, OPEN.capitalize()),
    )

    ONE_WINNER = 'one'
    TIERED = 'tiered'
    BET_TYPES = (
        (ONE_WINNER, ONE_WINNER.capitalize()),
        (TIERED, TIERED.capitalize())
    )

    event = models.ForeignKey(Event, blank=False, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False)
    start_time = models.DateTimeField(blank=False, null=False)
    status = models.CharField(max_length=16, choices=STATUSES, default=OPEN, null=False, blank=False)
    bet_type = models.CharField(max_length=16, choices=BET_TYPES, default=ONE_WINNER, null=False, blank=False)
    notes = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    results = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Matches'

    def __str__(self):
        return self.name


class MatchPlayer(BaseModel):
    match = models.ForeignKey(Match, blank=False, null=False, on_delete=models.RESTRICT)
    player = models.ForeignKey(Player, blank=False, null=False, on_delete=models.RESTRICT)


class MatchTeam(BaseModel):
    match = models.ForeignKey(Match, blank=False, null=False, on_delete=models.RESTRICT)
    team = models.ForeignKey(Team, blank=False, null=False, on_delete=models.RESTRICT)


class Bet(BaseModel):
    match = models.ForeignKey(Match, blank=False, null=False, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.RESTRICT)
    amount = models.IntegerField(blank=False, null=False)
    prediction = models.JSONField(blank=False, null=False)
