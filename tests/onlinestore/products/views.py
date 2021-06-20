# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from inspect import getmembers, isclass, isfunction, ismethod
from django.http import JsonResponse

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"


# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"

from .models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()  # We can also get a slice [:30]

    # Let's see what methds does the 'products' object have
    for (name, member) in getmembers(products, ismethod):
        if not name.startswith("_"):
            print(name)
            # print(member)

    # With the 'values' method, you can specify which columns to retrieve
    data = {"products": list(products.values("pk", "name"))}
    response = JsonResponse(data)
    return response
