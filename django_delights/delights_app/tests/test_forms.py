from django.test import TestCase
from delights_app.forms import *
from delights_app.models import *
from django.utils import timezone

class IngredientFormsTest(TestCase):
    def test_ingredient_create_form_valid(self):
        form_data = {'name': 'Test Ingredient', 'quantity': 100, 'unit': 'g', 'unit_price': 5}
        form = IngredientCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_ingredient_update_form_valid(self):
        ingredient = Ingredient.objects.create(name='Test Ingredient', unit='g')
        form_data = {'name': 'Updated Ingredient', 'quantity': 150, 'unit': 'kg', 'unit_price': 6}
        form = IngredientUpdateForm(data=form_data, instance=ingredient)
        self.assertTrue(form.is_valid())

class MenuItemFormsTest(TestCase):
    def test_menu_item_create_form_valid(self):
        form_data = {'name': 'Test Menu Item', 'price': 10}
        form = MenuItemCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_menu_item_update_form_valid(self):
        menu_item = MenuItem.objects.create(name='Test Menu Item')
        form_data = {'name': 'Updated Menu Item', 'price': 15}
        form = MenuItemUpdateForm(data=form_data, instance=menu_item)
        self.assertTrue(form.is_valid())

class RecipeRequirementsFormsTest(TestCase):
    def test_recipe_requirements_create_form_valid(self):
        menu_item = MenuItem.objects.create(name='Test Menu Item')
        ingredient = Ingredient.objects.create(name='Test Ingredient', unit='g')
        form_data = {'menu_item': menu_item.id, 'ingredient': ingredient.id, 'quantity': 2}
        form = RecipeRequirementsCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_recipe_requirements_update_form_valid(self):
        menu_item = MenuItem.objects.create(name='Test Menu Item2')
        ingredient = Ingredient.objects.create(name='Test Ingredient2', unit='g')
        req = RecipeRequirements.objects.create(menu_item=menu_item, ingredient=ingredient, quantity=2)
        form_data = {'menu_item': menu_item.id, 'ingredient': ingredient.id, 'quantity': 3}
        form = RecipeRequirementsUpdateForm(data=form_data, instance=req)
        self.assertTrue(form.is_valid())

class PurchaseFormsTest(TestCase):
    def test_purchase_create_form_valid(self):
        menu_item = MenuItem.objects.create(name='Test Menu Item')
        form_data = {'menu_item': menu_item.id, 'timestamp': timezone.now()}
        form = PurchaseCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_purchase_update_form_valid(self):
        menu_item = MenuItem.objects.create(name='Test Menu Item2')
        purchase = Purchase.objects.create(menu_item=menu_item)
        form_data = {'menu_item': menu_item.id, 'timestamp': timezone.now()}
        form = PurchaseUpdateForm(data=form_data, instance=purchase)
        self.assertTrue(form.is_valid())