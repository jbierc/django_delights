from datetime import datetime
from tkinter import CASCADE
from django.db import models

class Ingredient(models.Model):
    TEASPOON = "tsp"
    TABLESPOON = "tbsp"
    GRAMS = "g"
    KILOGRAMS = "kg"
    EGGS = "eggs"
    UNIT_TYPE_CHOICES = [(TEASPOON, "teaspoon"), (TABLESPOON, "tablespoon"), (GRAMS, "grams"), (KILOGRAMS, "kilograms"), (EGGS, "eggs")]
    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=4, choices=UNIT_TYPE_CHOICES, default=GRAMS)
    unit_price = models.FloatField(default=0.0)

class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)
