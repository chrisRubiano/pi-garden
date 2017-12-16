from django.urls import path
from . import views

app_name='sensors'
urlpatterns = [
    path('', views.all_sensors_view, name = 'all_sensors'),
]
