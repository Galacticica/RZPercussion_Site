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
        widget=forms.SelectMultiple(attrs={'class': 'multi-checkbox-dropdown-insts'}),  
        label="Instruments Used",
        required=False
    )
    type_query = forms.MultipleChoiceField(
        choices=[],  
        required=False,
        label="Select Piece Types",
        widget=forms.SelectMultiple(attrs={
            'class': 'multi-checkbox-dropdown-type',  
            'placeholder': 'Select Piece Types',
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


class SortForm(forms.Form):
    SORT_CHOICES = [
        ('newest', 'Date (Newest to Oldest)'),
        ('oldest', 'Date (Oldest to Newest)'),
        ('alphabetical', 'Alphabetical (A-Z)'),
    ]

    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'styled-radio'}),
        label="Sort by",
        required=False,
        initial='newest'
    )