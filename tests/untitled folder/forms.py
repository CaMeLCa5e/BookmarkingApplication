from django import forms
from .models import List, Link


class CreateListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ['name',]


class CreateLinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ['name', 'url', 'tags',]
