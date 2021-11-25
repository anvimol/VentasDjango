from django.urls import path

from core.views import myFirstView


urlpatterns = [
    path('uno/', myFirstView),
    path('dos/', myFirstView),
]