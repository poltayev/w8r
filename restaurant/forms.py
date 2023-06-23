from django import forms
from . import models

class RestaurantModelForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = models.Restaurant
        exclude = ('',)