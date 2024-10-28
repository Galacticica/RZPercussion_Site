from django.db import models




class Instruments(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Performers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Performed_Piece(models.Model):
    title = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    arranger = models.CharField(max_length=100, blank=True)
    performers = models.ManyToManyField(Performers, related_name='musical_pieces', blank=False)
    description = models.TextField()
    event = models.CharField(max_length=100, blank=True)
    link = models.URLField(max_length=200)
    piece_type = models.CharField(max_length=100)
    instruments = models.ManyToManyField(Instruments, related_name='musical_pieces')
    date = models.DateField(null=True, blank=True)
    music_link = models.URLField(max_length=200, blank=True)
    slug = models.SlugField(default="", null=False)
    

    def __str__(self):
        return self.title



