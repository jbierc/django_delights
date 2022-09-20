from django import forms
from .models import *

#ingredient forms
class IngredientCreateForm(forms.ModelForm):
  class Meta:
    model = Ingredient
    fields = ('name', 'quantity', 'unit', 'unit_price')

class IngredientUpdateForm(forms.ModelForm):
  class Meta:
    model = Ingredient
    fields = ('name', 'quantity', 'unit', 'unit_price')

#menuitem forms
class MenuItemCreateForm(forms.ModelForm):
  class Meta:
    model = MenuItem
    fields = ('name', 'price')

class MenuItemUpdateForm(forms.ModelForm):
  class Meta:
    model = MenuItem
    fields = ('name', 'price')

#reciperequirements forms
class RecipeRequirementsCreateForm(forms.ModelForm):
  class Meta:
    model = RecipeRequirements
    fields = ('menu_item', 'ingredient', 'quantity')

class RecipeRequirementsUpdateForm(forms.ModelForm):
  class Meta:
    model = RecipeRequirements
    fields = ('menu_item', 'ingredient', 'quantity')

#purchase forms
class PurchaseUpdateForm(forms.ModelForm):
  class Meta:
    model = Purchase
    fields = ('menu_item', 'timestamp')