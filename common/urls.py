from django.urls import path

from .views import CurrentDateView, HelloView, IndexView

urlpatterns = [
   path('', IndexView.as_view()),
   path('datetime/', CurrentDateView.as_view()),
   path('hello/', HelloView.as_view()),
]