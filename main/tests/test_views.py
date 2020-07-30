from decimal import Decimal
from main import models
from django.urls import reverse
from django.test import TestCase
class TestPage(TestCase):
    def test_products_page_returns_active(self):
        models.Product.objects.create(
            name="THe cathedral and bazaar",
            slug="cathedral-bazaar",
            price=Decimal("10.00")
        )
        models.Product.objects.create(
            name="A tale of two cities",
            slug="tale-of-two-cities",
            price=Decimal("2.00"),
            active=False
        )

        response = self.client.get(
            reverse("products", kwargs={"tag":"all"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BookTime")
        product_list = models.Product.objects.active().order_by(
            "name"
        )
        self.assertEqual(
            list(response.context["object_list"]),
            list(product_list)
        )

    def test_products_page_filter_by_tags_and_active(self):
        cb = models.Product.objects.create(
            name="THe cathedral and the bazaar",
            slug="cathedral-bazaar",
            price=Decimal("10.00")
        )
        cb.tags.create(name="Open source", slug="opensource")
        models.Product.objects.create(
            name="Microsoft Windows guide",
            slug="microsoft-windows-guide",
            price=Decimal("12.00")
        )
        response = self.client.get(
            reverse("products", kwargs={"tag":"opensource"})
        )
        self.assertEquals(response.status_code,200)
        self.assertContains(response, "BookTime")

        product_list = (
            models.Product.objects.active()
                                  .filter(tags__slug="opensource")
                                  .order_by("name")
        )
        self.assertEqual(
            list(response.context["object_list"]),
            list(product_list)
        )