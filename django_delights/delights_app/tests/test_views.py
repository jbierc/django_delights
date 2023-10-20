from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from delights_app.models import *
from datetime import datetime
from django.contrib.messages import get_messages
from django.contrib.auth.models import User


class PurchaseCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        #sample user
        self.user = User.objects.create_user(username='jbierc', password='adminadmin123')
        self.client.login(username='jbierc', password='adminadmin123')
        #populating database
        self.ingredient = Ingredient.objects.create(name='Test Ingredient', quantity=10, unit='grams')
        self.menu_item = MenuItem.objects.create(name='Test Menu Item')
        self.requirement = RecipeRequirements.objects.create(menu_item=self.menu_item, ingredient=self.ingredient, quantity=5)
        #setting url
        self.url = reverse('purchasecreate', kwargs={'pk': self.menu_item.id}) # type: ignore
        self.valid_post_data = {
            'menu_item': self.menu_item.id, # type: ignore
            'timestamp': datetime.now(tz=timezone.utc)
        }

    def test_successful_purchase_creation(self):
        response = self.client.post(self.url, data=self.valid_post_data, follow=True)
        self.assertEqual(response.status_code, 200) # Should successfully render template
        self.assertRedirects(response, reverse('menuitemlist'))
        # Check if a purchase was created
        self.assertTrue(Purchase.objects.filter(menu_item=self.menu_item).exists())

    def test_insufficient_ingredients(self):
        self.ingredient.quantity = 2  # Not enough quantity
        self.ingredient.save()

        response = self.client.post(self.url, data=self.valid_post_data, follow=True)

        self.assertEqual(response.status_code, 200)  # Should successfully render template
        self.assertRedirects(response, reverse('ingredientlist'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn('Not enough Test Ingredient 3.0 grams', str(messages[0]))

        # Check if a purchase was not created
        self.assertFalse(Purchase.objects.filter(menu_item=self.menu_item).exists())

class SummaryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='jbierc', password='adminadmin123')
        self.client.login(username='jbierc', password='adminadmin123')
        self.url = reverse('summary')
        self.menu_item = MenuItem.objects.create(name='Test Item', price=10)
        self.ingredient = Ingredient.objects.create(name='Test Ingredient', unit_price=5)
        self.requirement = RecipeRequirements.objects.create(menu_item=self.menu_item, ingredient=self.ingredient, quantity=2)
        self.purchase = Purchase.objects.create(menu_item=self.menu_item, timestamp=datetime.now(tz=timezone.utc))

    def test_summary_calculation(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        # Calculate expected revenue and cost based on the created objects
        revenue = self.purchase.menu_item.price
        cost = self.requirement.ingredient.unit_price * self.requirement.quantity
        profit = revenue - cost

        self.assertContains(response, f'{revenue}')
        self.assertContains(response, f'{cost}')
        self.assertContains(response, f'{profit}')