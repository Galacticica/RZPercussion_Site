"""
models.py
Reagan Zierke <reaganzierke@gmail.com>
12-04-2024
Creates the models for specific performances, instruments, piece types, instrument categories, and performers.
"""
from django.db import models

class InstrumentCategory(models.Model):
    '''
    This creates a model for the different categories of instruments. It is mainly used for sorting instruments by their type.
    '''
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category

# class InstrumentsQuerySet(models.QuerySet["Instruments"]):
#     pass

class Instrument(models.Model):
    '''
    This creates a model for all of the different instruments. It is used by the performance model and composition model.
    '''
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
    InstrumentCategory, 
    related_name='categorized_instruments', 
    on_delete=models.SET_DEFAULT, 
    default=1,
    blank=False
)
    # objects: InstrumentsQuerySet = InstrumentsQuerySet.as_manager()

    def __str__(self):
        return self.name


class Performer(models.Model):
    '''
    This creates a model for all of the different performers/groups. It is used by the performance model.
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PerformedPiece(models.Model):
    '''
    This creates the model for a performed piece. Most fields are required but some fields, such as arranger or music link, are not required as not every performance has those datapoints.
    It uses many to many fields for the instruments and performers, creating a relation between the piece and the instruments and performers models.
    '''
    title = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    arranger = models.CharField(max_length=100, blank=True)
    performers = models.ManyToManyField(Performer, related_name='musical_pieces', blank=False)
    description = models.TextField()
    event = models.CharField(max_length=100, blank=True)
    link = models.URLField(max_length=200)
    piece_type = models.CharField(max_length=100)
    instruments = models.ManyToManyField(Instrument, related_name='musical_pieces')
    date = models.DateField(null=True, blank=True)
    music_link = models.URLField(max_length=200, blank=True)
    slug = models.SlugField(default="", null=False)
    

    def __str__(self):
        return self.title



