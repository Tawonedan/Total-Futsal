from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = 'pages/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):

        if self.request.user.is_staff:

            return reverse_lazy('admin_dashboard')
        else:

            return reverse_lazy('user_home') 
        
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/register.html', {'form': form})

def home(request):
    return render(request, "pages/home.html", {})

def fields(request):
    return render(request, "pages/fields.html", {})

def accessories(request):
    return render(request, "pages/accessories.html", {})

def about(request):
    return render(request, "pages/about.html", {})

def contact(request):
    return render(request, "pages/contact.html", {})