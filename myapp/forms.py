from django import forms
from .models import Book

class FeedbackForm(forms.Form):
    FEEDBACK_CHOICES = [
        ('B', 'Borrow'),
        ('P', 'Purchase'),
    ]
    feedback =   forms.ChoiceField(choices = FEEDBACK_CHOICES)

from django import forms
from .models import Book

class SearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="Your Name"
    )

    category = forms.ChoiceField(
        choices=Book.CATEGORY_CHOICES,
        widget=forms.RadioSelect,
        required=False,
        label="Select a category:"
    )

    max_price = forms.IntegerField(
        required=True,
        min_value=0,
        label="Maximum Price"
    )
