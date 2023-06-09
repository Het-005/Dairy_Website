from django.contrib import admin
from django.urls import path
from Warehousemang import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("bill/", views.bill, name="bill detail"),
    path("profile/", views.profile, name="profile"),
    path("edit/", views.edit, name="edit order"),
    path("checkmilk/", views.checkmilk, name="Product view"),
]