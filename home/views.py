"""
views.py
Reagan Zierke <reaganzierke@gmail.com>
12-03-2024
Defines view for the (as of now unused) home page.
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def main(request):
  '''
  Renders the home page html file.
  '''
  template = loader.get_template('home/main.html')
  context={}
  return HttpResponse(template.render(context, request))