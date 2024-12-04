"""
models.py
Reagan Zierke <reaganzierke@gmail.com>
12-03-2024
Creates a model for a composition that includes any information that might be relevant to a composition.
"""
from django.db import models
from performances.models import Instrument

class Composition(models.Model):
    '''
    This is the model for the composition.
    '''
    title = models.CharField(max_length=100)
    og_composer = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    link = models.URLField(max_length=200)
    piece_type = models.CharField(max_length=100)
    instruments = models.ManyToManyField(Instrument, related_name='composed_pieces')
    complete = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)
    
    def __str__(self):
        return self.title
