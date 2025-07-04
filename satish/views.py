from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1>Welcome to Chai's Django Project: Home page</h1>")
    return render(request, 'websites/index.html')
def about(request):
    # return HttpResponse("<h1>Welcome to Chai's Django Project: Home page</h1>")
    return render(request, 'websites/about.html')

def contact(request):
    # return HttpResponse("<h1>Welcome to Chai's Django Project: Contact page</h1>")
    return render(request, 'websites/contact.html')