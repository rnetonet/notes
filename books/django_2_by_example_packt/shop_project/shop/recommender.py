from django.conf import settings

import redis

from .models import Product

r = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)

class Recommender:
    def get_product_key(self, id):
        return f"product:{id}:purchased_with"

    def products_bought(self, products):
        products_ids = products.values_list("id", flat=True)
        for product_id in products_ids:
            for companion_product_id in products_ids:
                if product_id != companion_product_id:
                    r.zincrby(self.get_product_key(product_id), amount=1, value=companion_product_id)

    def suggest_products_for(self, products, max_results=6):
        products_ids = products.values_list("id", flat=True)
        if len(products) == 1:
            suggestions = r.zrange(self.get_product_key(products_ids[0]), 0, -1, desc=True)[:max_results]
        else:
            # generate a temporary key
            flat_ids = ''.join([str(id) for id in product_ids])
            tmp_key = 'tmp_{}'.format(flat_ids)
            # multiple products, combine scores of all products
            # store the resulting sorted set in a temporary key
            keys = [self.get_product_key(id) for id in product_ids]
            r.zunionstore(tmp_key, keys)
            # remove ids for the products the recommendation is for
            r.zrem(tmp_key, *product_ids)
            # get the product ids by their score, descendant sort
            suggestions = r.zrange(tmp_key, 0, -1,
                                desc=True)[:max_results]
            # remove the temporary key
            r.delete(tmp_key)

        suggested_products_ids = [int(id) for id in suggestions]

        # get suggested products and sort by order of appearance
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x: suggested_products_ids.index(x.id))
        return suggested_products
