from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Equipment, Calculator
from .forms import CalculatorForm, EquipmentForm


def Index(request):
    return render(request, 'index.html', {})


# Calculator Views

class CalculatorListView(generic.ListView):
    model = Calculator
    queryset = Calculator.objects.order_by('make_and_model')
    template_name = 'calculator.html'


class CalculatorCreateView(generic.CreateView):
    model = Calculator
    form_class = CalculatorForm
    template_name = 'add-calculator.html'
    success_url = '/calculator/'


class CalculatorEditView(generic.UpdateView):
    model = Calculator
    form_class = CalculatorForm
    template_name = 'edit-calculator.html'
    success_url = '/calculator/'


# Equipment Views

class EquipmentListView(generic.ListView):
    model = Equipment
    queryset = Equipment.objects.filter(approved=True)
    template_name = 'equipment.html'


class EquipmentDetail(View):

    def get(self, request, slug, *args, **kwargs):
        equipment_info = Equipment.objects.all()
        equipment = get_object_or_404(equipment_info, slug=slug)

        return render(
            request,
            "equipment-detail.html",
            {'equipment': equipment},
        )
