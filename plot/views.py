from django.shortcuts import render
from django.views import generic

# Create your views here.


def plot(request):
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'plot/index.html',)