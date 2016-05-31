from django.forms import ModelForm
from .models import PointOfInterest


class PointOfInterestForm(ModelForm):

    class Meta:
        model = PointOfInterest
        fields = ['address', 'position']
