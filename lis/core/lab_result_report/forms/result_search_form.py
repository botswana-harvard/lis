from django import forms


class ResultSearchForm(forms.Form):
    result_search_term = forms.CharField(
        max_length=35,
        label="",
        help_text="enter all or part of a order number, sample identifier, patient identifier, etc",
        error_messages={'required': 'Please enter a search term.'},
        )
