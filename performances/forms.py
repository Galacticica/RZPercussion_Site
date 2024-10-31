from django import forms
from .models import Performed_Piece, Instruments

class PerformanceSearchForm(forms.Form):
    title_query = forms.CharField(max_length=255, required=False, label="Title")
    composer_query = forms.CharField(max_length=255, required=False, label="Composer / Arranger")
    instrument_query = forms.ModelMultipleChoiceField(queryset=Instruments.objects.all(), widget=forms.CheckboxSelectMultiple, label="Instruments Used", required=False)

    class Meta:
        model = Performed_Piece
        fields = ['title', 'composer', 'arranger', 'instruments']