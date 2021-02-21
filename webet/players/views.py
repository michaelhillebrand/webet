from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from players.models import Player


@require_http_methods(["GET"])
def player_list(request):

    players = Player.objects.all()

    response = {
        'players': [
            {
                'first_name': player.first_name,
                'last_name': player.last_name
            } for player in players
        ],
        'has_more': False
    }
    return JsonResponse(response)


def player_create(request):
    return HttpResponse("Success")


def player_read(request, player_id):
    return HttpResponse("Success")


def player_update(request, player_id):
    return HttpResponse("Success")


def player_delete(request, player_id):
    return HttpResponse("Success")
