from django.forms import ModelForm, DateTimeInput
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


class IncidentForm(ModelForm):
    date_time = forms.DateTimeField(
        widget=DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',  # You can add any class you need for styling
            'placeholder': 'Select Date and Time',
        })
    )
    class Meta:
        model = Incident
        fields = "__all__"
        labels = {
            'location': 'Location',  
            'date_time': 'Date Time',  
            'severity_level': 'Severity Level',
            'description': 'Description',
        }

