from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProducPhoto

from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    product_photo = ProducPhoto.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)


    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'product_photo': product_photo,
                   })

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    product_photo = ProducPhoto.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'product_photo': product_photo,
                   'cart_product_form': cart_product_form,
                   })