"""
admin.py
Reagan Zierke <reaganzierke@gmail.com>
12-03-2024
Registers performance models into the built in admin page.
"""
from django.contrib import admin

from .models import Performed_Piece, Instruments, Performers, InstrumentCategory


admin.site.register(Instruments)
admin.site.register(InstrumentCategory)
admin.site.register(Performers)

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    prepopulated_fields = {"slug" : ("title", "date")}

admin.site.register(Performed_Piece ,PerformanceAdmin)