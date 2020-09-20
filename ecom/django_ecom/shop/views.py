from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShopProduct 

# Create your views here.

def showAbout(request):
	return HttpResponse('Welcome to about page')

def shopTemplate(request):
	all_products = ShopProduct.objects.all()
	return render(request, 'shop.html', 
		{'all_items': all_products})

def addProduct(request):
	c = request.POST['content']
	new_item = ShopProduct(name = c)
	new_item.save()
	return HttpResponseRedirect('/shop/')

#def deleteProduct(request):
	#return HttpResponseRedirect('/shop/')