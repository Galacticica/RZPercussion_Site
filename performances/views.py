from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Performed_Piece 


def index(request):
    latest_performances = Performed_Piece.objects.order_by("-date")
    template = loader.get_template("performances/index.html")
    context = {"latest_performances" : latest_performances}
    return HttpResponse(template.render(context, request)) 

def performance(request, slug):
    piece = get_object_or_404(Performed_Piece, slug=slug)
    insts = [instrument.name for instrument in piece.instruments.all()]
    players = [performer.name for performer in piece.performers.all()].sort()
    print(players)
    template = loader.get_template("performances/performance.html")
    context = {"piece" : piece, "instruments" : insts, "players" : players}
    return HttpResponse(template.render(context, request))
