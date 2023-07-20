from django.test import SimpleTestCase
from django.urls import reverse, resolve
from delights_app.views import home, PasswordChange


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
       url = reverse('home')
       #print(resolve(url))
       self.assertEquals(resolve(url).func, home)

    def test_login_url_is_resolved(self):
       url = reverse('passwordchange')
       #print(resolve(url))
       self.assertEquals(resolve(url).func.view_class, PasswordChange)