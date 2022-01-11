from django.db import models

# Create 4 instance variables for storing object's data
class Item(models.Model):
    product_id = models.TextField()
    product_name = models.TextField()
    product_quantity = models.TextField()
    product_price = models.TextField()
