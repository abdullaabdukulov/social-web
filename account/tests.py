from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import LoginForm


class LoginTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_login_view(self):
        # Test that the login view returns a success status code
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # Test that the login form is being used in the template context
        self.assertTrue(isinstance(response.context['form'], LoginForm))

        # Test that a valid login attempt with the correct credentials logs the user in
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('home'))
        self.assertTrue('_auth_user_id' in self.client.session)

        # Test that an invalid login attempt with incorrect credentials does not log the user in
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse('_auth_user_id' in self.client.session)
