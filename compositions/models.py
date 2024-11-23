from django.db import models
from performances.models import Instruments

class Composition(models.Model):
    title = models.CharField(max_length=100)
    og_composer = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    link = models.URLField(max_length=200)
    piece_type = models.CharField(max_length=100)
    instruments = models.ManyToManyField(Instruments, related_name='composed_pieces')
    complete = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)
    
    def __str__(self):
        return self.title
