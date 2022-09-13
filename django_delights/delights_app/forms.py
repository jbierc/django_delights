from django import forms
from .models import *

class IngredientCreateForm(forms.ModelForm):
  class Meta:
    model = Ingredient
    fields = ('name', 'quantity', 'unit', 'unit_price')



