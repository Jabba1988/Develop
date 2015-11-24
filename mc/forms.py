# coding=utf-8
from django import forms
from .models import Cartridge


class CartridgeForm(forms.ModelForm):
    class Meta:
        model = Cartridge
        fields = ['Manufacturer', 'model', 'serial_number', 'date_of_filling', 'quality_of_filling']
