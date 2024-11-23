from django.contrib import admin
from .models import Composition

class CompositionAdmin(admin.ModelAdmin):
    list_display = ("title", "piece_type")
    prepopulated_fields = {"slug" : ("title", "piece_type")}

admin.site.register(Composition ,CompositionAdmin)