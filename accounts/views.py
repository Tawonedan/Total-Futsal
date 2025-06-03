from django.views import View
from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from .models import Lapangan, Tambahan, Jadwal
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from datetime import date


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

class UserContactView(LoginRequiredMixin, View):
    template_name = 'accounts/contact.html'

    def get(self, request):
        return render(request, self.template_name)

class UserBookView(LoginRequiredMixin, View):
    template_name = 'accounts/book.html'

    def get(self, request):
        tipe_filter = request.GET.get('tipe', 'semua')

        if tipe_filter == 'semua':
            lapangan_list = Lapangan.objects.all()
        else:
            lapangan_list = Lapangan.objects.filter(Tipe=tipe_filter)

        context = {
            'lapangan_list': lapangan_list,
            'filter_tipe_lapangan': tipe_filter,
        }

        return render(request, self.template_name, context)
    
class UserBookDetailView(LoginRequiredMixin, View):
    template_name = 'accounts/book_detail.html'

    def get(self, request, id):
        lapangan = get_object_or_404(Lapangan, pk=id)
        daftar_sesi = Jadwal.objects.all()
        daftar_item_tambahan = Tambahan.objects.all()
        context = {
            'lapangan': lapangan,
            'daftar_sesi': daftar_sesi,
            'daftar_item_tambahan': daftar_item_tambahan,
            'tanggal_main': request.GET.get('tanggal_main', ''),
        }

        return render(request, self.template_name, context)


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
