from inspect import getmembers, isclass, isfunction, ismethod
from django.http import JsonResponse

from .models import Product, Manufacturer


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {"manufacturers": list(manufacturers.values(
        "pk", "name", "location", "active"))}
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        data = {"manufacturer": {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active
        }}
        response = JsonResponse(data)
        return response
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Manufacturer not found!"
            }},
            status=404)
    return response


def product_list(request):
    products = Product.objects.all()  # We can also get a slice [:30]

    # This will show what methds does the 'products' object have
    # Down below, we will use the .values method
    for (name, member) in getmembers(products, ismethod):
        if not name.startswith("_"):
            print(name)
            # print(member)

    # With the 'values' method, you can specify which columns to retrieve
    data = {"products": list(products.values("pk", "name"))}
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "photo": product.photo.url,
            "price": product.price,
            "shipping_cost": product.shipping_cost,
            "quantity": product.quantity
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Product not found!"
            }},
            status=404)
    return response
