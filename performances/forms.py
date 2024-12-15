"""
forms.py
Reagan Zierke <reaganzierke@gmail.com>
12-03-2024
Creates a form that allows the user to filter by different pieces of information such as title, instruments, etc.
It also creates a form that allows the user to sort by newest-oldest, oldest-newest, or a-z
"""
from django import forms
from .models import PerformedPiece, Instrument

class PerformanceSearchForm(forms.Form):
    '''
    The performance search form uses a few different types of fields to allow the user to filter by title, composer, instruments, and piece type.
    '''
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
        queryset=Instrument.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'multi-checkbox-dropdown-insts'}),  
        label="Instruments Used",
        required=False
    )
    
    type_query = forms.MultipleChoiceField(
        choices=[],  
        required=False,
        label="Select Piece Types",
        widget=forms.SelectMultiple(attrs={
            'class': 'multi-checkbox-dropdown-piece-type',  
            'placeholder': 'Select Piece Types',
        })
    )

    def __init__(self, *args, **kwargs):
        '''
        Fills choices for piece type field.
        '''
        super().__init__(*args, **kwargs)
        piece_types = (
            PerformedPiece.objects
            .values_list('piece_type', flat=True)
            .distinct()
            .order_by('piece_type')  
        )
        self.fields['type_query'].choices = [(pt, pt) for pt in piece_types]

    class Meta:
        model = PerformedPiece
        fields = ['title', 'composer', 'arranger', 'instruments', 'piece_type']


class SortForm(forms.Form):
    '''
    The sort form has a radio select button that allows the user to choose how they want to sort the performances.
    '''
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