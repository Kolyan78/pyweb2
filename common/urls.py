from django.urls import path

from .views import CurrentDateView, HelloView

urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('hello/', HelloView.as_view()),
]