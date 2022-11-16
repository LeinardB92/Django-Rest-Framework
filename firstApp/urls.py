from django.urls import path
from . import views

urlpatterns = [
    path('emps/', views.employee_view),
]
