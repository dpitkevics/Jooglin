from django import forms

from GoogleSocialSearch.lib.forms import Form


class SearchForm(Form):
    query = forms.CharField(label='Search')