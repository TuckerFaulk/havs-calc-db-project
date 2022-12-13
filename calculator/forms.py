from .models import Calculator, Equipment
from django import forms


class CalculatorForm(forms.ModelForm):
    class Meta:
        model = Calculator
        fields = ('make_and_model', 'exposure_duration_hours', 'exposure_duration_minutes',)


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('make_and_model', 'category', 'author', 'vibration_magnitude', 'test_date', 'equipment_image',)
