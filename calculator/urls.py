from . import views
from django.urls import path


urlpatterns = [
    path('', views.Index, name='index'),
    path('calculator/', views.CalculatorListView.as_view(), name='calculator_list'),
    path('calculator/add/', views.CalculatorCreateView.as_view(), name='add_calculator'),
    path('calculator/<slug:slug>/edit', views.CalculatorEditView.as_view(), name='edit_calculator'),
    path('calculator/<slug:slug>/delete', views.CalculatorDeleteView.as_view(), name='delete_calculator'),
    path('equipment/', views.EquipmentListView.as_view(), name='equipment_list'),
    path('equipment/<slug:slug>/', views.EquipmentDetail.as_view(), name='equipment_detail'),
]
