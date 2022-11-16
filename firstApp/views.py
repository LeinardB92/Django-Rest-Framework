from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

# Create your views here.
def employee_view(request):
    emp = {
        'id': 123,
        'name': 'John',
        'sal': 5000
    }

    data = Employee.objects.all()
    response = {'employees': list(data.values('name', 'sal'))}

    # Consume datos, como el caso del dicionario de arriba, para selializarlos en un dato tipo JSON.
    return JsonResponse(response)