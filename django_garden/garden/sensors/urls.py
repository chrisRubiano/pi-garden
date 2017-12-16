from django.urls import path
from . import views

app_name='sensors'
urlpatterns = [
    path('', views.sensors_view, name = 'sensors'),
]
