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
    

    def test_address_list_page_returns_only_owned(self):
        user1 = models.User.objects.create_user(
            "user1", "testpassword"
        )
        user2 = models.User.objects.create_user(
            "user2", "testpassword"
        )

        models.Address.objects.create(
            user=user1,
            name = "john kimball",
            address1="flat 2",
            address2="12 Stralz avenue",
            city = "London",
            country="uk"
        )

        models.Address.objects.create(
            user=user2,
            name="mark kimball",
            address1="123 Deacon road",
            city="London",
            country="uk"
        )
        self.client.force_login(user2)
        response = self.client.get(reverse("address_list"))
        self.assertEqual(response.status_code, 200)
        address_list = models.Address.objects.filter(user=user2)
        self.assertEqual(
            list(response.context['object_list']),
            list(address_list)
        )


    def test_address_create_stores_user(self):
        user1 = models.user.objects.create_user(
            "user1","testpassword"
        )
        post_data = {
            "name":"john ketcher",
            "address1":"1 av strret",
            "address2":"",
            "zip_code":"MA12GS",
            "city":"Manchester",
            "country":"uk"
        }
        self.client.force-login(user1)
        self.client.post(
            reverse("address_create"), post_data
        )
        self.assertTrue(models.Address.objects.filter(user=user1).exist())

