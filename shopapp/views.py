from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Category, Product, Order

from django.shortcuts import render, get_object_or_404

# Create your views here.


#category 

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()  # Assuming you want to display the first 3 products
    return render(request, 'index.html', {'categories': categories, 'products': products})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})




#product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order_detail.html', {'order': order})

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'product_detail.html', {'product': product})
    
class CategoryProductsView(View):
    template_name="category_products.html"
    
    def get(self, request, category):
        products = Product.objects.filter(category__name=category)
        context = {'category': category, 'products': products}
        return render(request, self.template_name, context)
    
    
    

