from django import forms
from .models import *

class IngredientCreateForm(forms.ModelForm):
  class Meta:
    model = Ingredient
    fields = ('name', 'quantity', 'unit', 'unit_price')

class IngredientUpdateForm(forms.ModelForm):
  class Meta:
    model = Ingredient
    fields = ('name', 'quantity', 'unit', 'unit_price')

class MenuItemCreateForm(forms.ModelForm):
  class Meta:
    model = MenuItem
    fields = ('name', 'price')

class MenuItemUpdateForm(forms.ModelForm):
  class Meta:
    model = MenuItem
    fields = ('name', 'price')