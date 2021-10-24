from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def main_page(request):
    return render(request, 'website/layout.html')

def home(request):
	return render(request, 'website/home.html')

def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')