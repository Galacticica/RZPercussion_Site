"""
admin.py
Reagan Zierke <reaganzierke@gmail.com>
12-03-2024
Registers performance models into the built in admin page.
"""
from django.contrib import admin

from .models import PerformedPiece, Instrument, Performer, InstrumentCategory


admin.site.register(Instrument)
admin.site.register(InstrumentCategory)
admin.site.register(Performer)

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    prepopulated_fields = {"slug" : ("title", "date")}

admin.site.register(PerformedPiece ,PerformanceAdmin)