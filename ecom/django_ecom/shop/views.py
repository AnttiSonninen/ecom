from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def showAbout(request):
	return HttpResponse('Welcome to about page')

def shopTemplate(request):
	return render(request, 'shop.html')