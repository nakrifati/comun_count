from django import forms
from .model import *


class ComForm(forms.ModelForm):

    class Meta:
        model = Com
        exclude = [""]


class ComCostForm(forms.ModelForm):

    class Meta:
        model = ComCost
        exclude = [""]

