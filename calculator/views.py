from django.shortcuts import render
from django.views import generic
from .models import Equipment, Calculator


def Index(request):
    return render(request, 'index.html', {})


# Calculator Views


class CalculatorListView(generic.ListView):
    model = Calculator
    queryset = Calculator.objects.order_by('make_and_model')
    template_name = 'calculator.html'


# Equipment Views

class EquipmentListView(generic.ListView):
    model = Equipment
    queryset = Equipment.objects.filter(approved=True)
    template_name = 'equipment.html'
