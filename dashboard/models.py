from django.db import models
from django.contrib.auth.models import User

class EnergyConsumption(models.Model):
    date = models.DateField()
    time = models.TimeField()
    consumption = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    source_choices = [
        ('solar', 'Solar'),
        ('wind', 'Wind'),
        ('grid', 'Grid'),
        ('generator', 'Generator'),
    ]
    source = models.CharField(max_length=10, choices=source_choices)
    location = models.CharField(max_length=255)
    remarks = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="energy_consumptions")

    def __str__(self):
        return f"{self.date} - {self.location}"

class SavingsReport(models.Model):
    date = models.DateField()
    energy_saved = models.DecimalField(max_digits=10, decimal_places=2)
    savings = models.DecimalField(max_digits=10, decimal_places=2)
    method_choices = [
        ('energy_efficiency', 'Energy Efficiency'),
        ('load_shifting', 'Load Shifting'),
        ('demand_response', 'Demand Response'),
        ('renewable_sources', 'Renewable Sources'),
    ]
    method = models.CharField(max_length=20, choices=method_choices)
    percentage_saved = models.DecimalField(max_digits=5, decimal_places=2)
    units_saved = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="savings_reports")

    def __str__(self):
        return f"Savings Report on {self.date}"
