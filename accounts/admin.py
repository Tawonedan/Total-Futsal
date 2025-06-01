from django.contrib import admin
from .models import Pengguna, Jadwal, Lapangan, Tambahan, Pesanan, PesananTambahan

admin.site.register(Pengguna)
admin.site.register(Jadwal)
admin.site.register(Lapangan)
admin.site.register(Tambahan)
admin.site.register(Pesanan)
admin.site.register(PesananTambahan)
