"""
forms.py
Reagan Zierke <reaganzierke@gmail.com>
12-03-2024
Creates a form that allows the user to filter by different pieces of information such as title, instruments, etc.
"""
from django import forms
from .models import Composition, Instrument

class CompositionSearchForm(forms.Form):
    '''
    This is the filter form. It allows users to input a title, whether it is complete, and any isntruments used.
    '''
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
        queryset=Instrument.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'multi-checkbox-dropdown'}),  
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
            Composition.objects
            .values_list('piece_type', flat=True)
            .distinct()
            .order_by('piece_type')  
        )

        self.fields['type_query'].choices = [(pt, pt) for pt in piece_types]

    class Meta:
        model = Composition
        fields = ['title', 'complete', 'instruments', 'piece_type']