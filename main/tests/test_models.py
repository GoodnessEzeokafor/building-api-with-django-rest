from decimal import Decimal
from django.test import TestCase
from main import models

print("HELLO WORLD")
class TestModel(TestCase):
    def test_active_manager_works(self):
        models.Product.objects.create(
            name="The cathedral and the bazaar",
            price=Decimal("10.00")
        )
        models.Product.objects.create(
            name="Pride and prejudice",
            price=Decimal("2.00")
        )


        self.assertEqual(len(models.Product.objects.active()), 2)