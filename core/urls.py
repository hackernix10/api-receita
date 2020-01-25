from django.urls import path
from . import views

urlpatterns = [
    path('cpf/<str:NUM_CPF>/', views.CpfList.as_view(), name='cpf-list'),

]