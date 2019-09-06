from django.contrib import admin

from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "avaiable", "created", "updated")
    list_filter = ("avaiable", "created", "updated")
    list_editable = ["price", "avaiable"]
    prepopulated_fields = {"slug": ("name",)}
