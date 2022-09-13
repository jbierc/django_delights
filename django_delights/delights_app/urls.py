from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', include("django.contrib.auth.urls"), name='login'), #login, logout, password_change, password_reset
    path('logout/', views.logout_request, name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('ingredient/list', views.IngredientList.as_view(), name='ingredientlist'),
    path('ingredient/create', views.IngredientCreate.as_view(), name="ingredientcreate"),
    path('ingredient/update/<pk>', views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name="ingredientdelete")
]

