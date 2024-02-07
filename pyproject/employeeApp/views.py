from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse

from .models import *
from .serailizers import DepartmentSerializer, EmployeesSerializer

# Create your views here.

@csrf_exempt
def departmentAPI(request, id-0):
    if request.method == 'GET':
        departments= Departments.objects.all()
        departments_serializer= DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer= DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('Data added', safe=False)
        return JsonResponse('Unsuccessful', safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department= Departments.objects.get(DepartmentId=department_data['DepartmenId'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('Data updated', safe=False)
        return JsonResponse('Update is Unsuccessful', safe=False)
    
    elif  request.method == 'DELETE':
        department= Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse('Data updated', safe=False)
    else:
        return JsonResponse('iNVALID REQUEST', safe=False)
    