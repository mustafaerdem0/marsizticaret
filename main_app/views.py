from django.shortcuts import render
from .models import Product,Categories,Color
# Create your views here.

def index(request):
    return render(request,'index.html')


def product(request):
    products = Product.objects.filter(is_active = True)
    categorys = Categories.objects.all()
    colors = Color.objects.all()
    context = dict(
        products = products,
        categorys = categorys,
        colors = colors,
    )
    return render(request,'product.html',context)

def productfilter(request,category):
    products = Product.objects.filter(slug = category)
    context = dict(
        productfilter = products
    )
    return render(request,'product.html',context)
def card(request):
    return render(request,'shoping-cart.html')

def about(request):
    return render(request,'about.html')