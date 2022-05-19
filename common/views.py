from django.shortcuts import render

from datetime import datetime
from django.views import View
from django.http import HttpResponse
# Create your views here.
class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)

class HelloView(View):
    def get(self, request):
        hello = f"<h1>Hello, World</h1>"
        return HttpResponse(hello)