from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django import forms

from index.models import *
import json

# Create your views here.


def index(request):
    data = {}
    return render(request, 'delivery_detail.html', data)
