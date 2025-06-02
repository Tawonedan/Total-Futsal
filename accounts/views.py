from django.views import View
from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # Import LoginRequiredMixin


class UserHomeView(LoginRequiredMixin, View):
    template_name = 'accounts/user_home.html'

    def get(self, request):
        return render(request, self.template_name)


class UserProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/user_profile.html'

    def get(self, request):
        return render(request, self.template_name)

class UserProfileEditView(LoginRequiredMixin, View):
    template_name = 'accounts/user_profile_edit.html'

    def get(self, request):
        return render(request, self.template_name)


class UserAboutView(LoginRequiredMixin, View):
    template_name = 'accounts/about.html'

    def get(self, request):
        return render(request, self.template_name)

class UserBookView(LoginRequiredMixin, View):
    template_name = 'accounts/book.html'

    def get(self, request):
        return render(request, self.template_name)


class UserHistoryView(LoginRequiredMixin, View):
    template_name = 'accounts/history.html'

    def get(self, request):
        return render(request, self.template_name)


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'pages\templates\pages\home.html'
    next_page = 'home'


def register(request):
    return render(request, "accounts/register.html")

def user_profile(request):
    return render(request, "accounts/project_index.html")
