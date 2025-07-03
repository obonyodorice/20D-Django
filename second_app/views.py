from django.shortcuts import render

def home(request):
    return render(request, 'second_app/home.html')

