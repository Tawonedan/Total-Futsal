from django.urls import path
from pages import views
from .views import CustomLoginView, register

urlpatterns = [
    path("", views.home, name="home"),
    path("fields/", views.fields, name="fields"),
    path("accessories/", views.accessories, name="accessories"),
    path("about_us/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),

]