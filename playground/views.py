from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from store.models import Customer
from store.models import Collection
from store.models import Order


def say_hello(request):
    customer = Product.objects.filter(collection_id=3)

    return render(request, 'hello.html', {'name': 'Andrew', 'customers': list(customer)})
