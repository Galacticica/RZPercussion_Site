from django.contrib import admin

from .models import performed_piece, instruments

admin.site.register(performed_piece)
admin.site.register(instruments)