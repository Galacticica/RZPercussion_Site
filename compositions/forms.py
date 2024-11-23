from django import forms
from .models import Composition, Instruments

class CompositionSearchForm(forms.Form):
    title_query = forms.CharField(
        max_length=255,
        required=False,
        label="Title",
        widget=forms.TextInput(attrs={'class': 'styled-input'})  
    )
    complete_query = forms.BooleanField(
        required=False,  
        label="Is Complete",
        widget=forms.CheckboxInput(attrs={'class': 'styled-checkbox'})  
    )
    instrument_query = forms.ModelMultipleChoiceField(
        queryset=Instruments.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'multi-checkbox-dropdown'}),  
        label="Instruments Used",
        required=False
    )

    class Meta:
        model = Composition
        fields = ['title', 'complete', 'instruments']