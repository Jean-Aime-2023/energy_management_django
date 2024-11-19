# dashboard/forms.py
from django import forms
from .models import EnergyConsumption, SavingsReport

class EnergyConsumptionForm(forms.ModelForm):
    class Meta:
        model = EnergyConsumption
        fields = ['date', 'time', 'consumption', 'cost', 'source', 'location', 'remarks']

class SavingsReportForm(forms.ModelForm):
    class Meta:
        model = SavingsReport
        fields = ['date', 'energy_saved', 'savings', 'method', 'percentage_saved', 'units_saved', 'remarks']
