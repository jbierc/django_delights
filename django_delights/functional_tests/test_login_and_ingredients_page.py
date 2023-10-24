from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from delights_app.models import Ingredient
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from django.contrib.auth.models import User

class TestLoginAndIngredientsPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_login_and_no_ingredients(self):
        self.user = User.objects.create_user(username='jbierc', password='adminadmin123')

        self.browser.get(self.live_server_url)
        username = self.browser.find_element(By.ID, 'id_username')
        password = self.browser.find_element(By.ID, 'id_password')
        login_button = self.browser.find_element(By.ID, 'login_button')

        username.send_keys('jbierc')
        password.send_keys('adminadmin123')
        login_button.click()

        self.assertIn('Welcome jbierc', self.browser.page_source)
        
        ingredients = self.browser.find_element(By.ID, 'ingredients')
        ingredients.click()

        add_url = self.live_server_url + reverse('ingredientlist')
        self.assertEquals(self.browser.current_url, add_url)
        try:
            element = self.browser.find_element(By.TAG_NAME, "td")
            assert element is not None
        except NoSuchElementException:
            print("There is no ingredients")

    def test_ingredients(self):
        self.user = User.objects.create_user(username='jbierc', password='adminadmin123')
        self.ingredient = Ingredient.objects.create(name='Test Ingredient', quantity=10, unit='grams')

        self.browser.get(self.live_server_url)
        username = self.browser.find_element(By.ID, 'id_username')
        password = self.browser.find_element(By.ID, 'id_password')
        login_button = self.browser.find_element(By.ID, 'login_button')

        username.send_keys('jbierc')
        password.send_keys('adminadmin123')
        login_button.click()

        ingredients = self.browser.find_element(By.ID, 'ingredients')
        ingredients.click()

        self.assertEquals(self.browser.find_element(By.TAG_NAME, "td").text, 'Test Ingredient')
           
