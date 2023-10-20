from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from delights_app.views import *


class TestUrls(SimpleTestCase):
    def setUp(self):
       self.client = Client()

    def test_home_url_is_resolved(self):
       url = reverse('home')
       self.assertEquals(resolve(url).func, home)
       self.assertTemplateUsed('home.html')

    def test_login_url_is_resolved(self):
       url = reverse('login')
       response = self.client.get(url)
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'registration/login.html')
       
    def test_logout_url_is_resolved(self):
       url = reverse('logout')
       response = self.client.get(url)
       self.assertEqual(response.status_code, 302)

    def test_passwordchange_url_is_resolved(self):
       url = reverse('passwordchange')
       response = self.client.get(url)
       self.assertEquals(resolve(url).func.view_class, PasswordChange)
       self.assertTemplateUsed(response, 'registration/password_change.html')

    def test_summary_url_is_resolved(self):
       url = reverse('summary')
       self.assertEquals(resolve(url).func, Summary)
       self.assertTemplateUsed('summary.html')