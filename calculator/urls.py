from . import views
from django.urls import path


urlpatterns = [
    path('', views.Index, name='index'),
    path('calculator/', views.CalculatorListView.as_view(), name='calculator_list'),
]
