from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Performed_Piece, Instruments


def index(request):
    latest_performances = Performed_Piece.objects.order_by("-date")[:5]
    
    template = loader.get_template("performances/index.html")
    context = {"latest_performances" : latest_performances}
    return HttpResponse(template.render(context, request)) 

def performance(request, performed_piece_id):
    return HttpResponse("You're looking at piece %s" % performed_piece_id)