from django.db import models




class Instruments(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Performed_Piece(models.Model):
    title = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(max_length=200)
    piece_type = models.CharField(max_length=100)
    instruments = models.ManyToManyField(Instruments, related_name='musical_pieces')
    date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.title



