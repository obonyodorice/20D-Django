from django.shortcuts import render
from .models import Attachee

def index(request):
    return render(request, 'first_app/index.html')

def attachee_view(request):
    attachee_data = Attachee.objects.all()

    context = {
        'attachee_data': attachee_data
    }

    return render(request, 'first_app/attachee_view.html', context)