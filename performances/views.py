from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Performed_Piece 
from .forms import TitleSearchForm

def index(request):
    performances = Performed_Piece.objects.order_by("-date")
    title_search_form = TitleSearchForm(request.GET)
    template = loader.get_template("performances/index.html")
    if title_search_form.is_valid():
        query = title_search_form.cleaned_data['query']
        performances = performances.filter(title__icontains=query)
    context = {"performances" : performances, "title_search_form" : title_search_form}
    return HttpResponse(template.render(context, request)) 

def performance(request, slug):
    piece = get_object_or_404(Performed_Piece, slug=slug)
    insts = [instrument.name for instrument in piece.instruments.all()]
    players = [performer.name for performer in piece.performers.all()]
    players.sort()
    template = loader.get_template("performances/performance.html")
    context = {"piece" : piece, "instruments" : insts, "players" : players}
    return HttpResponse(template.render(context, request))
