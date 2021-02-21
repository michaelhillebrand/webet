from django.contrib import admin

from .models import *

admin.site.register(EventPlayer)
admin.site.register(EventTeam)
admin.site.register(EventTeamMembership)
admin.site.register(EventUser)

admin.site.register(MatchTeam)
admin.site.register(MatchPlayer)

admin.site.register(Bet)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "start_time", "end_time")


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("name", "event", "start_time", "status", "bet_type")
    list_filter = ("event",)
