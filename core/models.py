from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
