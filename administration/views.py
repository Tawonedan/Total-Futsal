from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Pesanan, Lapangan, Tambahan
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import datetime

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
        lapangan_list = Lapangan.objects.all()
        context = {
            'lapangan_list': lapangan_list
        }
        return render(request, self.template_name, context)

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
        tambahan_list = Tambahan.objects.all()
        context = {
            'tambahan_list': tambahan_list
        }
        return render(request, self.template_name, context)

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
        context = {}
        
        # Ambil semua pesanan yang statusnya selesai (misal status=0 adalah selesai)
        # Sesuaikan dengan definisi status di model Anda
        # Jika status 0 = Selesai, 1 = Berlangsung, 2 = Dibatalkan
        pesanan_selesai = Pesanan.objects.filter(status=0) 

        # Pendapatan Bulan Ini
        current_month = timezone.now().month
        current_year = timezone.now().year
        pendapatan_bulan_ini = pesanan_selesai.filter(
            Tanggal__year=current_year, Tanggal__month=current_month
        ).aggregate(total=Sum('total_harga'))['total'] or 0
        context['total_pendapatan_bulan_ini'] = pendapatan_bulan_ini

        # Booking Selesai Bulan Ini
        jumlah_transaksi_bulan_ini = pesanan_selesai.filter(
            Tanggal__year=current_year, Tanggal__month=current_month
        ).count()
        context['jumlah_transaksi_bulan_ini'] = jumlah_transaksi_bulan_ini

        # Total Pendapatan Keseluruhan
        total_pendapatan_keseluruhan = pesanan_selesai.aggregate(total=Sum('total_harga'))['total'] or 0
        context['total_pendapatan_keseluruhan'] = total_pendapatan_keseluruhan
        
        # Filter (Contoh Dasar)
        # Anda perlu membuat Django Form untuk menangani filter ini dengan lebih baik
        filter_tanggal_mulai_str = request.GET.get('tanggal_mulai')
        filter_tanggal_akhir_str = request.GET.get('tanggal_akhir')
        filter_lapangan_id = request.GET.get('filter_lapangan')
        filter_status_pesanan = request.GET.get('filter_status_pesanan')

        transaksi_list = Pesanan.objects.all().select_related('id_user', 'ID_lapangan', 'id_jadwal').order_by('-Tanggal', '-Jam')

        if filter_tanggal_mulai_str:
            transaksi_list = transaksi_list.filter(Tanggal__gte=datetime.strptime(filter_tanggal_mulai_str, '%Y-%m-%d').date())
        if filter_tanggal_akhir_str:
            transaksi_list = transaksi_list.filter(Tanggal__lte=datetime.strptime(filter_tanggal_akhir_str, '%Y-%m-%d').date())
        if filter_lapangan_id:
            transaksi_list = transaksi_list.filter(ID_lapangan_id=filter_lapangan_id)
        if filter_status_pesanan != '' and filter_status_pesanan is not None:
            transaksi_list = transaksi_list.filter(status=filter_status_pesanan)
            
        context['transaksi_list'] = transaksi_list
        context['lapangan_options'] = Lapangan.objects.all() # Untuk dropdown filter
        
        # Simpan nilai filter untuk ditampilkan kembali di form
        context['filter_values'] = {
            'tanggal_mulai': filter_tanggal_mulai_str or '',
            'tanggal_akhir': filter_tanggal_akhir_str or '',
            'lapangan': filter_lapangan_id or '',
            'status_pesanan': filter_status_pesanan if filter_status_pesanan is not None else '',
        }

        return render(request, self.template_name, context)




class AdminHistoryView(LoginRequiredMixin, View):
    template_name = 'administration/admin_riwayat.html'

    def get(self, request):
        return render(request, self.template_name)

class AdminHistoryDetailView(LoginRequiredMixin, View):
    template_name = 'administration/admin_riwayat_detail.html'

    def get(self, request):
        return render(request, self.template_name)