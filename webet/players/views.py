from django.http import HttpResponse

from players.models import Player


def player_list(request):
    all_players = Player.objects.all()
    output = ', '.join([p.name for p in all_players])
    return HttpResponse(output)


def player_create(request):
    return HttpResponse("Success")


def player_read(request, player_id):
    return HttpResponse("Success")


def player_update(request, player_id):
    return HttpResponse("Success")


def player_delete(request, player_id):
    return HttpResponse("Success")
