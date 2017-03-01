from django.shortcuts import render
import json
import django.http
from django.core import serializers
from books.models import FoodItems
from django.http import HttpResponse

def getObject(request):
    data = serializers.serialize('json', FoodItems.objects.all())
    return HttpResponse(data, content_type='application/json')
