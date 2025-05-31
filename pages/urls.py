from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name="home"),
    path("fields/", views.fields, name="fields"),
    path("accessories/", views.accessories, name="accessories"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

]