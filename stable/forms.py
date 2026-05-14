from django import forms
from .models import HorseTour

class TourForm(forms.ModelForm):
    class Meta:
        model = HorseTour
        fields = '__all__'