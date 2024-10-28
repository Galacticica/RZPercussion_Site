from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Performed_Piece


def index(request):
    latest_performances = Performed_Piece.objects.order_by("-date")
    template = loader.get_template("performances/index.html")
    context = {"latest_performances" : latest_performances}
    return HttpResponse(template.render(context, request)) 

def performance(request, performed_piece_id):
    piece = get_object_or_404(Performed_Piece, pk=performed_piece_id)
    insts = [instrument.name for instrument in piece.instruments.all()]
    template = loader.get_template("performances/performance.html")
    context = {"piece" : piece, "instruments" : insts}
    return HttpResponse(template.render(context, request))
