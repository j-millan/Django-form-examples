from django.test import TestCase
from forms import models, views, forms
from django.urls import resolve, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
# Create your tests here.

class SignUpTests(TestCase):
    def setUp(self):
        self.url = reverse('forms:sign_up')
        self.response = self.client.get(self.url)

    def test_sign_up_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_sign_up_url_resolves_sign_up_view(self):
        view = resolve(self.url)
        self.assertEquals(view.func, views.sign_up)

    def test_sign_up_view_contains_link_to_login_page(self):
        login_url = reverse('forms:login')
        self.assertContains(self.response, 'href="{0}"'.format(login_url))

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, forms.SignUpForm)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_new_user_valid_post_data(self):
        data  = {
            'username' : 'j-millan',
            'email' : 'test@case.com',
            'password1' : 'peacesign',
            'password2' : 'peacesign'
        }

        self.client.post(self.url, data)
        self.assertTrue(User.objects.exists())
