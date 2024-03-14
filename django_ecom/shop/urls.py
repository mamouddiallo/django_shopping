from django.contrib import admin
from django.urls import path
from . import views
from .views import shop, panier, commande

urlpatterns = [
   path('', views.shop, name="shop"),
   path('panier/',views.panier, name="panier"),
   path('commande/',views.commande, name="commande"),
]