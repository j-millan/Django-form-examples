from django.test import TestCase
from forms import models, views, forms
from django.urls import resolve, reverse

# Create your tests here.

def SignUpTests(TestCase):
    def setUp(self):
        self.url = reverse('forms:sign_up')
        self.response = self.get(self.url)

    def test_sign_up_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_sign_up_url_resolves_sign_up_view(self):
        view = resolve(self.url)
        self.assertEquals(view.func, views.sign_up)

    def test_sign_up_view_contains_link_to_login_page(self):
        login_url = reverse('forms:login')
        self.assertContains(self.response, 'href="{0}"'.format())

def LoginTests(TestCase):
    def setUp(self):
        self.url = reverse('forms:login')
        self.response = self.client.get(self.url)

    def test_login_view_status_code(self):
        return self.assertEquals(self.response.status_code, 200)

    def test_login_url_resolves_login_view(self):
        view = resolve(self.url)
        self.assertEquals(view.func, views.login)

    def test_login_view_contains_link_to_sign_up_page(self):
        sign_up_url = reverse('forms:sign_up')
        self.assertContains(self.response, 'href="{0}"'.format(sign_up_url))