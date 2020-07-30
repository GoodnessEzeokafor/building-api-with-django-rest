from django.test import TestCase
from django.core import mail
from main import forms

from unittest.mock import patch
from django.contrib import auth


class TesForm(TestCase):
    def test_valid_contact_us_form_send_email(self):
        form = forms.ContactForm({
            'name':"Goodness Ezeokafor",
            'message':"Hi There"
        })
        self.assertTrue(form.is_valid())


        with self.assertLogs('main.forms', level='INFO') as cm:
            form.send_mail()
        self.assertEqual(len(mail.outbox),1)
        self.assertEqual(mail.outbox[0].subject, 'Site message')
        self.assertGreaterEqual(len(cm.output), 1)

    

    def test_invalid_contact_us_form(self):
        form = forms.ContactForm({
            'message':"Hi There"
        })
        self.assertFalse(form.is_valid())


    def test_user_signup_page_submission_works(self):
        post_data = {
            "email":"user@domain.com",
            "password1":"abecdfkslsdml",
            "password2":"abecdfkslsdml"
        }
        with patch.object(
            forms.UserCreationForm,"send_mail"
        ) as mock_send:
            response = self.client.post(
                reverse("signup"), post_data
            )
            self.assertEqual(response.status_code, 302)
            self.assertTrue(
                models.user.objects.filter(email="user@domain.com").exists()
            )
            self.assertTrue(
                auth.get_user(self.client).is_authenticated
            )
        mock_send.assert_called_once()