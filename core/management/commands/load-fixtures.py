from random import randint
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import Product
import itertools


class Builder:
    def __init__(self):
        self._product_count = itertools.count()

    def product(self, name=None, price=None, description=None, commit=False):
        product_count = next(self._product_count)
        product = Product(
            name=name or f"Product {product_count}",
            description=description or f"Description for product {product_count}",
            price=price or randint(1, 100),
        )
        if commit:
            product.save()
        return product


class Command(BaseCommand):
    help = "Removes all data and creates default products in the database."

    def add_arguments(self, parser):
        parser.add_argument(
            "-c",
            "--count",
            nargs="?",
            dest="count",
            type=int,
            help="Number of products to create",
            default=100,
        )

    @transaction.atomic
    def handle(self, *args, count, **options):
        call_command("flush", interactive=False)
        builder = Builder()
        products = [builder.product() for _ in range(count)]
        Product.objects.bulk_create(products)
