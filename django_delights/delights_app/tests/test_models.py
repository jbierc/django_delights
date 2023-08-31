from django.test import TestCase
from delights_app.models import *
from django.utils import timezone
from datetime import datetime

class IngredientModelTest(TestCase):
    def setUp(self):
        self.ingredient = Ingredient(name='Test Ingredient', unit='g')
    def test_str_representation(self):
        self.assertEqual(str(self.ingredient), 'Test Ingredient (g)')
    def test_absolute_url(self):
        self.assertEqual(self.ingredient.get_absolute_url(), '/ingredient/list')

class MenuItemModelTest(TestCase):
    def setUp(self):
        self.menu_item = MenuItem(name='Test Menu Item')
    def test_str_representation(self):
        self.assertEqual(str(self.menu_item), 'Test Menu Item')
    def test_absolute_url(self):
        self.assertEqual(self.menu_item.get_absolute_url(), '/menuitem/list')

class RecipeRequirementsModelTest(TestCase):
    def setUp(self):
        self.ingredient = Ingredient(name='Test Ingredient', unit='g')
        self.menu_item = MenuItem(name='Test Menu Item')
        self.recipe_requirements = RecipeRequirements(menu_item=self.menu_item, ingredient=self.ingredient, quantity=2)
    def test_str_representation(self):
        self.assertEqual(str(self.recipe_requirements), '2 g Test Ingredient (g) for Test Menu Item')
    def test_absolute_url(self):
        self.assertEqual(self.recipe_requirements.get_absolute_url(), '/reciperequirements/list')

class PurchaseModelTest(TestCase):
    def setUp(self):
        self.menu_item = MenuItem(name='Test Menu Item')
        self.purchase = Purchase(menu_item=self.menu_item, timestamp=datetime.now(tz=timezone.utc))
    def test_str_representation(self):
        self.assertEqual(str(self.purchase), f'Test Menu Item {self.purchase.timestamp}')
    def test_absolute_url(self):
        self.assertEqual(self.purchase.get_absolute_url(), '/purchase/list')
    