"""
views.py
Reagan Zierke <reaganzierke@gmail.com>
12-04-2024
Creates the views for the performances part of the site. As of now, filtering also takes place here.
"""
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader
from django.db.models import Q, Count
from django.shortcuts import redirect
from .models import PerformedPiece 
from .forms import PerformanceSearchForm, SortForm

def index(request):
    '''
    This provides the view for the index of performances page. It loads the index html file and then gathers all performance objects.
    If the filter form was filled out, it will filter the performances based on what the user input. 
    Additionally if the sort button was selected, it will sort the performances.
    It then renders the template, providing the forms and objects in the context.
    '''
    performances = PerformedPiece.objects.order_by("-date")
    performances = performances.filter(is_public=True)
    performance_search_form = PerformanceSearchForm(request.GET)
    sort_form = SortForm(request.GET)
    template = loader.get_template("performances/index.html")

    if performance_search_form.is_valid():
        title_query = performance_search_form.cleaned_data['title_query']
        composer_query = performance_search_form.cleaned_data['composer_query']
        instrument_query = performance_search_form.cleaned_data['instrument_query']
        type_query = performance_search_form.cleaned_data['type_query']
        performances = performances.filter(title__icontains=title_query)
        performances = performances.filter(Q(composer__icontains=composer_query) | Q(arranger__icontains=composer_query))

        if instrument_query:
            performances = performances.filter(instruments__in=instrument_query).distinct()
            performances = performances.annotate(
            instrument_count=Count('instruments', distinct=True)
            ).filter(
            instrument_count=len(instrument_query)
            )

        if type_query:
            performances = performances.filter(piece_type__in=type_query)

    if sort_form.is_valid():
        sort_by = sort_form.cleaned_data['sort_by']

        if sort_by == 'newest':
            performances = performances.order_by('-date')

        elif sort_by == 'oldest':
            performances = performances.order_by('date')  

        elif sort_by == 'alphabetical':
            performances = performances.order_by('title') 

    context = {"performances" : performances, "performance_search_form" : performance_search_form, "sort_form" : sort_form}
    return HttpResponse(template.render(context, request)) 

def performance(request, slug):
    '''
    This provides the view for the specific performance.
    It provides the specific chosen piece as well as the instruments and players in that piece in the context.
    It then renders the html template.

    Parameters
    ----------
    slug : the unique id for the url of the performance
    '''
    piece = get_object_or_404(PerformedPiece, slug=slug)

    players = [performer.name for performer in piece.performers.all()]
    players.sort()

    insts = [instrument.name for instrument in piece.instruments.all()]
    insts.sort()
    
    template = loader.get_template("performances/performance.html")
    context = {"piece" : piece, "instruments" : insts, "players" : players}
    return HttpResponse(template.render(context, request))
