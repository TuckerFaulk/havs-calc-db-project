from django.shortcuts import render
from django.views import generic
from .models import Equipment, Calculator


def Index(request):
    return render(request, 'index.html', {})


class CalculatorListView(generic.ListView):
    model = Calculator
    queryset = Calculator.objects.order_by('make_and_model')
    template_name = 'calculator.html'
