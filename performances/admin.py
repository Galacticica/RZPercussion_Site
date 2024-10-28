from django.contrib import admin

from .models import Performed_Piece, Instruments


admin.site.register(Instruments)

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    prepopulated_fields = {"slug" : ("title", "date")}

admin.site.register(Performed_Piece ,PerformanceAdmin)