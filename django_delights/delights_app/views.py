from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate


def login_view(request):
  context = {"login_view": "active"}

  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
 
    user = authenticate(request, username=username, password=password)
 
    if user is not None:
      return redirect("home.html")
    else:
      return HttpResponse("Invalid credentials!")
  
  return render(request, "registration/login.html", context)


def home(request):
    return HttpResponse("Hello!")