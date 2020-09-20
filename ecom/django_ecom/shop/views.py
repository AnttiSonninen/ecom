from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShopProduct 

import random

# Create your views here.

def showAbout(request):
	return HttpResponse('Welcome to about page')

def shopTemplate(request):
	all_products = ShopProduct.objects.all()
	sum = 0
	for product in all_products:
		sum += product.price
	return render(request, 'shop.html', 
		{'all_items': all_products, 'sum': sum})

def addProduct(request):
	c = request.POST['content']
	p = random.randint(1, 9)
	new_item = ShopProduct(name = c, price = p)
	new_item.save()
	return HttpResponseRedirect('/shop/')

def deleteProduct(request, product_id):
	item_to_delete = ShopProduct.objects.get(id=product_id) 	
	item_to_delete.delete()
	return HttpResponseRedirect('/shop/')

def buyCart(request):
	all_products = ShopProduct.objects.all()
	sum = 0
	for product in all_products:
		sum += product.price	
	return render(request, 'buy.html', 
		{'all_items': all_products, 'sum': sum})

def completed(request):
	all_products = ShopProduct.objects.all()
	sum = 0
	for product in all_products:
		sum += product.price	
	return render(request, 'completed.html', 
		{'all_items': all_products, 'sum': sum})	