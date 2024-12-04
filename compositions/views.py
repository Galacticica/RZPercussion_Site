"""
views.py
Reagan Zierke <reaganzierke@gmail.com>
12-03-2024
Creates the views for the composition part of the site. As of now, filtering also takes place here.
"""
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader
from django.db.models import Q, Count
from django.shortcuts import redirect
from .models import Composition 
from .forms import CompositionSearchForm

def index(request):
    '''
    This view is for the index of all of the compositions. It filters any fields that may have been filled out in the form. 
    It provides the context needed for the html template and renders the template.
    '''
    compositions = Composition.objects.order_by('title')
    composition_search_form = CompositionSearchForm(request.GET)
    template = loader.get_template("compositions/index.html")
    if composition_search_form.is_valid():
        title_query = composition_search_form.cleaned_data['title_query']
        complete_query = composition_search_form.cleaned_data.get('complete_query')
        instrument_query = composition_search_form.cleaned_data['instrument_query']
        type_query = composition_search_form.cleaned_data['type_query']
        compositions = compositions.filter(title__icontains=title_query)
        if complete_query:
            compositions = compositions.filter(complete=True)
        if instrument_query:
            compositions = compositions.filter(instruments__in=instrument_query).distinct()
            compositions = compositions.annotate(
            instrument_count=Count('instruments', distinct=True)
            ).filter(
            instrument_count=len(instrument_query)
            )
        if type_query:
            compositions = compositions.filter(piece_type__in=type_query)
    context = {"compositions" : compositions, "composition_search_form" : composition_search_form}
    return HttpResponse(template.render(context, request))


def composition(request, slug):
    '''
    This view is for a specific composition.
    It provides a specific composition object, as well as the instruments in the composition and renders the composition html template.

    Parameters
    ----------
    
    slug : the unique id for the url of the composition

    '''
    piece = get_object_or_404(Composition, slug=slug)
    template = loader.get_template("compositions/composition.html")
    insts = [instrument.name for instrument in piece.instruments.all()]
    insts.sort()
    context = {"piece" : piece, "instruments" : insts}
    return HttpResponse(template.render(context, request))