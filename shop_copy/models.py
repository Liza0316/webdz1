from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    class Meta:
        db_table = 'shop_copy_product'