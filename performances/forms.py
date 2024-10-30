from django import forms

class TitleSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)