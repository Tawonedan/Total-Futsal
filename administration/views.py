from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

class AdminDashboardView(LoginRequiredMixin, View):
    template_name = 'administration/admin_dashboard.html'

    def get(self, request):
        return render(request, self.template_name)

class AdminProfileView(LoginRequiredMixin, View):
    template_name = 'administration/admin_profil.html'

    def get(self, request):
        return render(request, self.template_name)
    
class AdminProfileEditView(LoginRequiredMixin, View):
    template_name = 'administration/admin_edit_profil.html'

    def get(self, request):
        return render(request, self.template_name)
    
    
class AdminFieldsView(LoginRequiredMixin, View):
    template_name = 'administration/admin_data_lapangan.html'

    def get(self, request):
        return render(request, self.template_name)

class AdminFieldsAddView(LoginRequiredMixin, View):
    template_name = 'administration/admin_tambah_lapangan.html'

    def get(self, request):
        return render(request, self.template_name)

class AdminFieldsEditView(LoginRequiredMixin, View):
    template_name = 'administration/admin_edit_lapangan.html'

    def get(self, request):
        return render(request, self.template_name)
    
    
class AdminAccessoriesView(LoginRequiredMixin, View):
    template_name = 'administration/admin_data_peralatan.html'

    def get(self, request):
        return render(request, self.template_name)

class AdminAccessoriesAddView(LoginRequiredMixin, View):
    template_name = 'administration/admin_tambah_peralatan.html'

    def get(self, request):
        return render(request, self.template_name)

class AdminAccessoriesEditView(LoginRequiredMixin, View):
    template_name = 'administration/admin_edit_peralatan.html'

    def get(self, request):
        return render(request, self.template_name)
        

class AdminReportView(LoginRequiredMixin, View):
    template_name = 'administration/admin_laporan.html'

    def get(self, request):
        return render(request, self.template_name)


class AdminHistoryView(LoginRequiredMixin, View):
    template_name = 'administration/admin_riwayat.html'

    def get(self, request):
        return render(request, self.template_name)

class AdminHistoryDetailView(LoginRequiredMixin, View):
    template_name = 'administration/admin_riwayat_detail.html'

    def get(self, request):
        return render(request, self.template_name)