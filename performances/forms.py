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
    type_query = forms.ChoiceField(
        choices=[],  
        required=False,
        label="Select Piece Type",
        widget=forms.Select(attrs={
        'class': 'styled-input',
        'placeholder': 'Select Piece Type',
    })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        piece_types = (
        Performed_Piece.objects
        .values_list('piece_type', flat=True)
        .distinct()
        .order_by('piece_type')  
    )
        self.fields['type_query'].choices = [(pt, pt) for pt in piece_types]

    class Meta:
        model = Performed_Piece
        fields = ['title', 'composer', 'arranger', 'instruments', 'piece_type']