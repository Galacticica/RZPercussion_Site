from django.shortcuts import render

from django.http import HttpResponse

from .models import performed_piece, instruments


def index(request):
    
    return HttpResponse("Hello, world. You're at the performances index.") 

def performance(request, performed_piece_id):
    return HttpResponse("You're looking at piece %s" % performed_piece_id)