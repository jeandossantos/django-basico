from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

import json
# Create your views here.
def show_products(request):
    
    if request.method == 'GET': 
        return render(request, 'products.html',{
            "products":[
            {
                "id": 1,
                "name": "products 1",
            },
            {
                "id": 2,
                "name": "products 2",
            }
        ]})
    elif request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        
        return HttpResponse(json.dumps({"name": name, "age": age}))
    
def add_product(request):
    return HttpResponse("Produto adicionado.")