from django.core.exceptions import ValidationError

from django import forms
from .models import CustomPackage

class CustomPackageForm(forms.ModelForm):
    nameCustomPackage = forms.CharField(label='Enter your name', widget=forms.TextInput(
        attrs={'class': 'validate', 'type': 'text', 'id': 'nameCustomPackage'}
    ))
    emailCustomPackage = forms.EmailField(label='Enter your email', widget=forms.EmailInput(
        attrs={'class': 'validate', 'type': 'email', 'id': 'emailCustomPackage'}
    ))
    phoneCustomPackage = forms.IntegerField(label='Enter your phone', widget=forms.TextInput(
        attrs={'class': 'validate', 'type': 'number', 'id': 'phoneCustomPackage'}
    ))
    guestCustomPackage = forms.IntegerField(label='Guest total', widget=forms.TextInput(
        attrs={'class': 'validate', 'type': 'number', 'id': 'guestCustomPackage'}
    ))
    placeCustomPackage = forms.CharField(label='Select City or Place', widget=forms.TextInput(
        attrs={'class': 'autocomplete validate', 'type': 'text', 'id': 'placeCustomPackage'}
    ))
    LIST_SELECTEDCUSTOMPACKAGE = (
        ('Regular Package', 'Regular Package'),
        ('Honeymoon Package', 'Honeymoon Package'),
        ('Family Package', 'Family Package'),
        ('Holiday Package', 'Holiday Package'),
    )
    selectedCustomPackage = forms.ChoiceField(label='Select your package', choices = LIST_SELECTEDCUSTOMPACKAGE)

    arrivalCustomPackage = forms.DateField(label='Arrival Date', widget=forms.DateInput(
        attrs={'class': 'validate', 'type': 'text', 'id': 'from', 'readonly' : ''}
    ))
    departureCustomPackage = forms.DateField(label='Departure Date', widget=forms.DateInput(
        attrs={'class': 'validate', 'type': 'text', 'id': 'to', 'readonly' : ''}
    ))
    minpriceCustomPackage = forms.FloatField(label='Min Price', widget=forms.TextInput(
        attrs={'class': 'validate', 'type': 'number', 'id': 'minpriceCustomPackage'}
    ))
    maxpriceCustomPackage = forms.IntegerField(label='Max Price', widget=forms.TextInput(
        attrs={'class': 'validate', 'type': 'number', 'id': 'maxpriceCustomPackage'}
    ))

    class Meta:
        model = CustomPackage
        fields = (
            'nameCustomPackage', 'emailCustomPackage', 'phoneCustomPackage', 'guestCustomPackage', 'placeCustomPackage', 'selectedCustomPackage', 'arrivalCustomPackage', 'departureCustomPackage', 'minpriceCustomPackage', 'maxpriceCustomPackage')