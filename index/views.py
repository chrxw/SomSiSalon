from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.db.models import Max
from django.db import connection
from index.models import *
import json


# Create your views here.

def index(request):
    data = {}
    return render(request, 'index.html', data)


class CustomerList(View):
    def get(self, request):
        customers = list(Customer.objects.all().values())
        data = dict()
        data['customers'] = customers
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class CustomerDetail(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        data = dict()
        data['customers'] = model_to_dict(customer)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class EmployeeList(View):
    def get(self, request):
        employees = list(Employee.objects.all().values())
        data = dict()
        data['employees'] = employees
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class EmployeeDetail(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        data = dict()
        data['employee'] = model_to_dict(employee)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response
