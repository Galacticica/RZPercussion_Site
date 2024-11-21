from django import forms
from .models import Performed_Piece, Instruments

class PerformanceSearchForm(forms.Form):
    title_query = forms.CharField(
        max_length=255,
        required=False,
        label="Title",
        widget=forms.TextInput(attrs={'class': 'styled-input'})  
    )
    composer_query = forms.CharField(
        max_length=255,
        required=False,
        label="Composer / Arranger",
        widget=forms.TextInput(attrs={'class': 'styled-input'})  
    )
    instrument_query = forms.ModelMultipleChoiceField(
        queryset=Instruments.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'multi-checkbox-dropdown'}),  
        label="Instruments Used",
        required=False
    )

    class Meta:
        model = Performed_Piece
        fields = ['title', 'composer', 'arranger', 'instruments']