from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# Create your views here.
def products_list(request, category_slug=None):
    products = Product.objects.filter(avaiable=True)
    categories = Category.objects.all()

    category = None
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)

    return render(
        request,
        "shop/product/list.html",
        {"category": category, "categories": categories, "products": products},
    )


def product_detail(request, id, product_slug):
    product = get_object_or_404(Product, id=id, slug=product_slug, avaiable=True)
    return render(request, "shop/product/detail.html", {"product": product})

