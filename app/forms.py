from django import forms
from .models import *

class ItemInfoForms(forms.ModelForm):
    class Meta:
        model= ItemInfo
        fields = "__all__"