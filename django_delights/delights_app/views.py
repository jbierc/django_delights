from email import message
from re import template
from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
from .forms import *

#account views
@login_required
def home(request):
  return render(request, "home.html")

def logout_request(request):
  logout(request)
  return redirect("home")

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"
  
class PasswordChange(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/password_change.html"

#ingredient views
class IngredientList(LoginRequiredMixin, ListView):
  model = Ingredient

class IngredientCreate(LoginRequiredMixin, CreateView):
  model = Ingredient
  template_name = "delights_app/ingredient_create_form.html"
  form_class = IngredientCreateForm

class IngredientUpdate(LoginRequiredMixin, UpdateView):
  model = Ingredient
  template_name = "delights_app/ingredient_update_form.html"
  form_class = IngredientUpdateForm

class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  template_name = "delights_app/ingredient_delete_form.html"
  success_url = reverse_lazy("ingredientlist")

#menuitem views
class MenuItemList(LoginRequiredMixin, ListView):
  model = MenuItem

class MenuItemCreate(LoginRequiredMixin, CreateView):
  model = MenuItem
  template_name = "delights_app/menuitem_create_form.html"
  form_class = MenuItemCreateForm

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
  model = MenuItem
  template_name = "delights_app/menuitem_update_form.html"
  form_class = MenuItemUpdateForm

class MenuItemDelete(LoginRequiredMixin, DeleteView):
  model = MenuItem
  template_name = "delights_app/menuitem_delete_form.html"
  success_url = reverse_lazy("menuitemlist")

#reciperequirements views
class RecipeRequirementsList(LoginRequiredMixin, ListView):
  model = RecipeRequirements

class RecipeRequirementsCreate(LoginRequiredMixin, CreateView):
  model = RecipeRequirements
  template_name = "delights_app/reciperequirements_create_form.html"
  form_class = RecipeRequirementsCreateForm

class RecipeRequirementsUpdate(LoginRequiredMixin, UpdateView):
  model = RecipeRequirements
  template_name = "delights_app/reciperequirements_update_form.html"
  form_class = RecipeRequirementsUpdateForm

class RecipeRequirementsDelete(LoginRequiredMixin, DeleteView):
  model = RecipeRequirements
  template_name = "delights_app/reciperequirements_delete_form.html"
  success_url = reverse_lazy("reciperequirementslist")

#purchase views
class PurchaseList(LoginRequiredMixin, ListView):
  model = Purchase

@login_required
def PurchaseCreate(request, pk=0):
  #current MenuItem and it's RecipeRequirements
  item = MenuItem.objects.get(id=pk)
  all_requirements = RecipeRequirements.objects.filter(menu_item=item)

  if request.method == 'POST':
    #calculating inv.
    restock = []
    for requirements in all_requirements:
      if requirements.quantity <= requirements.ingredient.quantity:
        requirements.ingredient.quantity -= requirements.quantity
      else:
        #adding number of needed ingr. units to restock
        restock.append(requirements.ingredient.name + ' ' + str(requirements.quantity - requirements.ingredient.quantity) + ' ' + requirements.ingredient.unit)
    #alerting if not enough ingr.    
    if restock:
      messages.warning(request, f'Not enough {", ".join(restock)}')
      return redirect('ingredientlist') #HttpResponse(f'Not enough {", ".join(restock)}')
    else:
      for requirements in all_requirements:
        requirements.ingredient.save()
    #adding new purchase
    newPurchase = Purchase()
    newPurchase.menu_item_id = request.POST['menu_item']  # type: ignore
    newPurchase.timestamp = request.POST['timestamp']
    newPurchase.save()
    messages.success(request, f'Successfully added {newPurchase.menu_item.name} purchase.')
    return redirect('menuitemlist')

  #adding current menu_item context to form
  context = {}
  initial_dict = { "menu_item":item }
  context['form'] = PurchaseCreateForm(request.POST or None, initial=initial_dict)
  template_name = "delights_app/purchase_create_form.html"
  return render(request, template_name, context)

class PurchaseUpdate(LoginRequiredMixin, UpdateView):
  model = Purchase
  template_name = "delights_app/purchase_update_form.html"
  form_class = PurchaseUpdateForm

class PurchaseDelete(LoginRequiredMixin, DeleteView):
  model = Purchase
  template_name = "delights_app/purchase_delete_form.html"
  success_url = reverse_lazy("purchaselist")

@login_required
def Summary(request):

  revenue = 0
  cost = 0
  all_purchases = Purchase.objects.all()
  for purchase in all_purchases:
    revenue += purchase.menu_item.price
    menu_item_req = RecipeRequirements.objects.filter(menu_item = purchase.menu_item)
    for req in menu_item_req:
      cost += (req.ingredient.unit_price * req.quantity)
  profit = round(revenue - cost, 2)

  context = { 'revenue': revenue, 'cost': cost, 'profit':profit }
  template_name = "delights_app/summary.html"
  return render(request, template_name, context)