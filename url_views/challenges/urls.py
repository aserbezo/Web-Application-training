from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # /challenges/
    path('<int:month>', views.montly_challange_by_number),
    path('<str:month>', views.montly_challange , name= 'month-challenge'),
]