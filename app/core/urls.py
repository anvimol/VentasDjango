from django.urls import path

from core.views import myFirstView, mySecondView

app_name = 'core'

urlpatterns = [
    path('uno/', myFirstView, name='vista1'),
    path('dos/', mySecondView, name='vista2'),
]