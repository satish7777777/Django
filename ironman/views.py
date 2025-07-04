from django.shortcuts import render

# Create your views here.

def all_ironman(request):
    return render(request, 'ironman/all_ironman.html')