"""
views.py
Reagan Zierke <reaganzierke@gmail.com>
12-03-2024
Defines view for about me page.
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def about(request):
  '''
  This is the view for the about me page
  '''
  template = loader.get_template('aboutme/about.html')
  context={}
  return HttpResponse(template.render(context, request))