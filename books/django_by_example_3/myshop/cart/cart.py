from decimal import Decimal

from django.conf import settings

from shop.models import Product


class Cart:
    def __init__(self, request):
        """
        Init the cart.
        """
        self.session = request.session
        self.cart = self.session.get(settings.CART_SESSION_ID)
        if not self.cart:
            self.cart = self.session[settings.CART_SESSION_ID] = {}

    def __iter__(self):
        """
        Iterate over cart items.
        """
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)

        cart = self.cart.copy()

        for product in products:
            cart_item = cart[str(product.id)]
            cart_item["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Cart's total number of items.
        """
        return sum(item["quantity"] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": quantity, "price": str(product.price)}
        elif override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.save()

    def remove(self, product: Product):
        """
        Removes a product from the cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        """
        Cart items total price.
        """
        total_price = Decimal("0.0")
        for item in self:
            total_price += Decimal(item["total_price"])

        return total_price

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.save()