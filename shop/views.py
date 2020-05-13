from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def allProdCat(request, c_slug = None):
    c_page = None
    products = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug = c_slug)
        products = Product.objects.filter(category = c_page, available = True)
    else:
        products = Product.objects.all().filter(available = True)
    context = {'catergory':c_page, 'products':products}
    print (context)
    return render (request, 'shop/category.html', context)

def ProdCatDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Esception as e:
        raise e
    context = {'product':product}
    return render (request, 'shop/product.html', context)