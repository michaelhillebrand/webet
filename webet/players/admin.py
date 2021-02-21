from django.contrib import admin

from .models import Player, Team, Membership

admin.site.register(Team)
admin.site.register(Membership)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "prefix", "suffix", "version")

    # def show_average(self, obj):
    #     from django.db.models import Avg
    #     result = Player.objects.filter(person=obj).aggregate(Avg("grade"))
    #     return result["grade__avg"]

