from django.test import TestCase
from .models import Ingredient

# Create your tests here.
class IngredientTests(TestCase):
    def test_ingredient_unit(self):
        new_ingredient = Ingredient(name = 'egg', unit = 'tbsp')
        new_ingredient.full_clean()
        