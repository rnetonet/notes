from django.urls import path

from . import views

app_name = "shop"
urlpatterns = [
    path("", views.products_list, name="products_list"),
    path(
        "<slug:category_slug>/", views.products_list, name="products_list_by_category"
    ),
    path("<int:id>/<slug:product_slug>/", views.product_detail, name="product_detail"),
]
