from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404, render

from .models import Category, Product


# Create your views here.
def product_list(request, category_slug=None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category__slug=category_slug)

    return render(
        request,
        "shop/product/list.html",
        {"products": products, "category": category, "categories": categories},
    )


def product_detail(request, id, slug):
    cart_add_product_form = CartAddProductForm()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(
        request,
        "shop/product/detail.html",
        {"product": product, "cart_add_product_form": cart_add_product_form},
    )
