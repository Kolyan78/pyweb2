from django.urls import path

from .views import RandomValue

urlpatterns = [
   path('random/', RandomValue.as_view()),
]