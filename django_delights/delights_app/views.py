from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
from .forms import *

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

@login_required
def home(request):
  return render(request, "home.html")

def logout_request(request):
  logout(request)
  return redirect("home")

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

#purchase views