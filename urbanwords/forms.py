from django import forms


class WordSearchForm(forms.Form):
    term = forms.CharField(label='Search for a term', max_length=100)
