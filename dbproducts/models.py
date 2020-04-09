from django.db import models
from django.db.models import Count

class ProductManager(models.Manager):
    def substitute(self, product):
        """ This function returns 6 different substitutes for 'prod_name'"""
        prod = product.id
        cat = Category.objects.filter(product__id=prod)

        all_products = Product.objects.filter(categories__in=cat).annotate(num_cat=Count("categories")).distinct().exclude(id=prod).exclude(nutri_grade__gte=Product.objects.get(id=prod).nutri_grade).order_by('-num_cat')
        # We can change later "gte" to "gt" for more product answers

        return all_products[:6]


class Category(models.Model):
    """Class that allows a classification of products"""
    name = models.CharField(max_length=100)

class Product(models.Model):
    """Class of product models"""

    id = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=250)
    img_front_url = models.URLField(max_length=255)
    nutri_grade = models.IntegerField()
    img_nutrition_url = models.URLField(max_length=255)
    web_link = models.URLField(max_length=255)
    categories = models.ManyToManyField("Category")
    # Add manager to Product
    objects = ProductManager()
