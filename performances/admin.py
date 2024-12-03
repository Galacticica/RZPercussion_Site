from django.contrib import admin

from .models import Performed_Piece, Instruments, Performers, InstrumentCategory, PieceType


admin.site.register(Instruments)
admin.site.register(InstrumentCategory)
admin.site.register(Performers)
admin.site.register(PieceType)

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    prepopulated_fields = {"slug" : ("title", "date")}

admin.site.register(Performed_Piece ,PerformanceAdmin)