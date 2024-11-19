from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import EnergyConsumption, SavingsReport
from .forms import EnergyConsumptionForm, SavingsReportForm # type: ignore
from django.db.models import Sum
from django.db.models import F

def dashboard(request):
    current_consumption = EnergyConsumption.objects.filter(user=request.user).order_by('-date').first()
    current_saving = SavingsReport.objects.filter(user=request.user).order_by('-date').first()

    total_consumption = EnergyConsumption.objects.filter(user=request.user).aggregate(Sum('consumption'))['consumption__sum'] or 0
    total_saving = SavingsReport.objects.filter(user=request.user).aggregate(Sum('savings'))['savings__sum'] or 0

    consumptions = EnergyConsumption.objects.filter(user=request.user).order_by('date')[:10]
    savings = SavingsReport.objects.filter(user=request.user).order_by('date')[:10]

    consumption_dates = [consumption.date.strftime("%Y-%m-%d") for consumption in consumptions]
    consumption_values = [float(consumption.consumption) for consumption in consumptions]
    saving_values = [float(saving.savings) for saving in savings]

    context = {
        'current_consumption': current_consumption,
        'current_saving': current_saving,
        'total_consumption': total_consumption,
        'total_saving': total_saving,
        'dates': consumption_dates,  
        'consumption_data': consumption_values,  
        'savings_data': saving_values,  
    }

    return render(request, 'energy/dashboard.html', context)



def add_consumption(request):
    if request.method == 'POST':
        form = EnergyConsumptionForm(request.POST)
        if form.is_valid():
            consumption = form.save(commit=False)
            consumption.user = request.user  
            consumption.save()
            print("Redirecting to consumption")
            return redirect('consumption')  
        else:
            print(form.errors)
    else:
        form = EnergyConsumptionForm()
    return render(request, 'energy/add_consumption.html', {'form': form})

def consumption_list(request):
    consumptions = EnergyConsumption.objects.filter(user=request.user)
    return render(request, 'energy/consumption.html', {'consumptions': consumptions})

def update_consumption(request, pk):
    consumption = get_object_or_404(EnergyConsumption, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EnergyConsumptionForm(request.POST, instance=consumption)
        if form.is_valid():
            form.save()
            return redirect('consumption')  
    else:
        form = EnergyConsumptionForm(instance=consumption)
    return render(request, 'energy/update_consumption.html', {'form': form})

def delete_consumption(request, pk):
    consumption = get_object_or_404(EnergyConsumption, pk=pk, user=request.user)
    if request.method == 'POST':
        consumption.delete()
        return redirect('consumption')  
    return render(request, 'energy/confirm_delete.html', {'object': consumption})

def add_saving(request):
    if request.method == 'POST':
        form = SavingsReportForm(request.POST)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.user = request.user  
            saving.save()
            return redirect('saving')  
        else:
            print(form.errors)
    else:
        form = SavingsReportForm()
    return render(request, 'energy/add_saving.html', {'form': form})

def savings_list(request):
    savings = SavingsReport.objects.filter(user=request.user)
    return render(request, 'energy/saving.html', {'savings': savings})

def update_saving(request, pk):
    saving = get_object_or_404(SavingsReport, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SavingsReportForm(request.POST, instance=saving)
        if form.is_valid():
            form.save()
            return redirect('saving')  
    else:
        form = SavingsReportForm(instance=saving)
    return render(request, 'energy/update_saving.html', {'form': form})

def delete_saving(request, pk):
    saving = get_object_or_404(SavingsReport, pk=pk, user=request.user)
    if request.method == 'POST':
        saving.delete()
        return redirect('saving') 
    return render(request, 'energy/confirm_delete.html', {'object': saving})
