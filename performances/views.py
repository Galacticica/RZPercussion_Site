from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader
from django.db.models import Q, Count
from django.shortcuts import redirect
from .models import Performed_Piece 
from .forms import PerformanceSearchForm

def index(request):
    performances = Performed_Piece.objects.order_by("-date")
    performance_search_form = PerformanceSearchForm(request.GET)
    template = loader.get_template("performances/index.html")
    if performance_search_form.is_valid():
        title_query = performance_search_form.cleaned_data['title_query']
        composer_query = performance_search_form.cleaned_data['composer_query']
        instrument_query = performance_search_form.cleaned_data['instrument_query']
        performances = performances.filter(title__icontains=title_query)
        performances = performances.filter(Q(composer__icontains=composer_query) | Q(arranger__icontains=composer_query))
        if instrument_query:
            performances = performances.filter(instruments__in=instrument_query).distinct()
            performances = performances.annotate(
            instrument_count=Count('instruments', distinct=True)
            ).filter(
            instrument_count=len(instrument_query)
            )
    context = {"performances" : performances, "performance_search_form" : performance_search_form}
    return HttpResponse(template.render(context, request)) 

def performance(request, slug):
    piece = get_object_or_404(Performed_Piece, slug=slug)
    insts = [instrument.name for instrument in piece.instruments.all()]
    players = [performer.name for performer in piece.performers.all()]
    players.sort()
    template = loader.get_template("performances/performance.html")
    context = {"piece" : piece, "instruments" : insts, "players" : players}
    return HttpResponse(template.render(context, request))
