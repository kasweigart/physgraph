from django.urls import path

from . import views

app_name = 'plot'

urlpatterns = [
    path('', views.plot, name='plot'),
]

