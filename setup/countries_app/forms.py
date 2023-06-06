from django import forms

from .models import (
    Trip,
    Comment,
)

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['country', 'private_comment']

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.fields['private_comment'].required = False

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['trip', 'comment']
        widgets = {
            'trip': forms.HiddenInput()
        }
    