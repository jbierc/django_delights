from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


"""
def login_view(request):
  context = {"login_view": "active"}

  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
 
    user = authenticate(request, username=username, password=password)
 
    if user is not None:
      login(request, user)
      return redirect("home.html")
    else:
      return HttpResponse("Invalid credentials!")
  
  return render(request, "registration/login.html", context)
"""


@login_required
def home(request):
  return render(request, "home.html")

def logout_request(request):
  logout(request)
  return redirect("home")  