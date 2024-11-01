from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def main(request):
  print(f"User authenticated: {request.user.is_authenticated}")
  print(f"User: {request.user}")
  print(f"Session data: {request.session.items()}")

  template = loader.get_template('home/main.html')
  context={}
  return HttpResponse(template.render(context, request))