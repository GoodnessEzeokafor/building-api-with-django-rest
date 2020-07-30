from django.test import TestCase
from django.urls import reverse
from main import forms
# Create your tests here.


class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, 'BookTime') 

    def test_about_us_page(self):
        response = self.client.get("/about-us")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")
        self.assertContains(response, 'BookTime')
    

    def test_contact_us_page_works(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")
        # self.assertContains(response, )
        self.assertIsInstance(
            response.context['form'], forms.ContactForm
        )