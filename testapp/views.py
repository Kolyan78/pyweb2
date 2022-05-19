from django.shortcuts import render

from random import random
from django.views import View
from django.http import HttpResponse
# Create your views here.
class RandomValue(View):
    def get(self, request):
        random_number = round(random() * 100, 2)
        return HttpResponse(random_number)
