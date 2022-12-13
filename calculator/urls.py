from . import views
from django.urls import path


urlpatterns = [
    path('', views.Index, name='index'),
    path('calculator/', views.CalculatorListView.as_view(), name='calculator_list'),
    path('calculator/add/', views.CalculatorCreateView.as_view(), name='add_calculator'),
    path('calculator/<slug:slug>/edit', views.CalculatorEditView.as_view(), name='edit_calculator'),
    path('calculator/<slug:slug>/delete', views.CalculatorDeleteView.as_view(), name='delete_calculator'),
    path('equipment/', views.EquipmentListView.as_view(), name='equipment_list'),
    path('equipment/add/', views.EquipmentCreateView.as_view(), name='add_equipment'),
    path('equipment/<slug:slug>/', views.EquipmentDetail.as_view(), name='equipment_detail'),
    path('equipment/<slug:slug>/edit', views.EquipmentEditView.as_view(), name='edit_equipment'),
    path('equipment/<slug:slug>/delete', views.EquipmentDeleteView.as_view(), name='delete_equipment'),
]
