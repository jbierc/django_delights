from datetime import datetime
from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class RecipeRequirements(models.Model):
    ingredients_list = models.ForeignKey(MenuItem.ingredients, on_delete=models.CASCADE)

class Purchase(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(default=datetime.date.today)
