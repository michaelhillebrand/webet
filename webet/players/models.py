from django.db import models

from base.models import BaseModel
from tags.models import Tag


class Player(BaseModel):
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    prefix = models.CharField(max_length=8, blank=True, null=True)
    suffix = models.CharField(max_length=8, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.first_name + (f" {self.last_name}" if self.last_name else '')


class Team(BaseModel):
    name = models.CharField(max_length=128, blank=False, null=False)
    members = models.ManyToManyField(
        Player,
        through='Membership',
        through_fields=('team', 'player'),
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    team = models.ForeignKey(Team, blank=False, null=False, on_delete=models.RESTRICT)
    player = models.ForeignKey(Player, blank=False, null=False, on_delete=models.RESTRICT)
    position = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.team} - {self.player}"
