from django.shortcuts import render

from django.http import HttpResponse

from .models import Performed_Piece, Instruments


def index(request):
    latest_performances = Performed_Piece.objects.order_by("-date")[:5]
    output = ", ".join([p.title for p in latest_performances])
    return HttpResponse(output) 

def performance(request, performed_piece_id):
    return HttpResponse("You're looking at piece %s" % performed_piece_id)