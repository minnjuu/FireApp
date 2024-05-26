from django.forms import ModelForm
from django import forms
from fire.models import Locations, Incident, FireStation

class FireStationForm(ModelForm):
    class Meta:
        model = FireStation
        fields = "__all__"
        labels = {
            'name': 'Fire Station Name',  
            'latitude': 'Latitude',  
            'longitude': 'Longitude',
            'address': 'Address',
            'city': 'City',
            'country': 'Country',
        }