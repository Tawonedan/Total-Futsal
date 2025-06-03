# futsal_booking/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Custom User Manager untuk model Pengguna
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) # Penting untuk hashing password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('Level', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# Model Pengguna sebagai model User utama
class Pengguna(AbstractBaseUser, PermissionsMixin):
    ID = models.AutoField(primary_key=True)
    Nama = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    # HAPUS BARIS INI: Password = models.CharField(max_length=20)
    Level = models.CharField(max_length=5, default='user')

    Alamat = models.TextField(blank=True, null=True)
    Telepon = models.CharField(max_length=20, blank=True, null=True)
    NIP = models.CharField(max_length=50, unique=True, blank=True, null=True)

    # Ubah ke ImageField dan direktori lebih spesifik
    gambar = models.FileField(upload_to='user_images/', blank=True, null=True)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Nama']

    class Meta:
        db_table = 'users'
        verbose_name_plural = "Pengguna"

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.Level == 'admin' or self.is_superuser

# ====================================================================
# Models lainnya (sesuai skema SQL Anda)
# ====================================================================

class Jadwal(models.Model):
  id_jadwal = models.AutoField(primary_key=True)
  Jadwal = models.CharField(max_length=255)
  mulai = models.TimeField(null=True, blank=True)
  akhir = models.TimeField(null=True, blank=True)

  class Meta:
    db_table = 'jadwal'
    verbose_name_plural = "Jadwal"

  def __str__(self):
    return self.Jadwal

class Lapangan(models.Model):
  ID = models.AutoField(primary_key=True)
  Nama = models.CharField(max_length=255)
  Tipe = models.CharField(max_length=255)
  Jenis = models.CharField(max_length=255)
  Harga = models.IntegerField()
  status = models.IntegerField(default=1)
  # Ubah ke ImageField dan direktori lebih spesifik
  gambar = models.FileField(upload_to='lapangan_images/', blank=True, null=True)


  class Meta:
    db_table = 'lapangan'
    verbose_name_plural = "Lapangan"

  def __str__(self):
    return self.Nama

class Tambahan(models.Model):
  ID = models.AutoField(primary_key=True)
  Nama = models.CharField(max_length=255)
  Harga = models.IntegerField()
  # Ini sudah bagus, biarkan
  gambar = models.FileField(upload_to='tambahan_images/', blank=True, null=True)


  class Meta:
    db_table = 'tambahan'
    verbose_name_plural = "Tambahan"

  def __str__(self):
    return self.Nama

class Pesanan(models.Model):
  ID = models.AutoField(primary_key=True)
  id_user = models.ForeignKey(Pengguna, on_delete=models.CASCADE, db_column='id_user')
  ID_lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE, db_column='ID_lapangan')
  id_jadwal = models.ForeignKey(Jadwal, on_delete=models.CASCADE, db_column='id_jadwal')
  tambahan_items = models.ManyToManyField(Tambahan, through='PesananTambahan')
  Nama = models.CharField(max_length=20)
  Telepon = models.CharField(max_length=20)
  Jam = models.TimeField()
  durasi = models.IntegerField()
  Tanggal = models.DateField()
  total_harga = models.IntegerField()
  bayar = models.IntegerField()
  kembali = models.IntegerField()
  status = models.IntegerField()

  class Meta:
    db_table = 'pesanan'
    verbose_name_plural = "Pesanan"

  def __str__(self):
    return f"Pesanan ID: {self.ID} - {self.Nama}"
  
class PesananTambahan(models.Model):
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE)
    item = models.ForeignKey(Tambahan, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'pesanan_tambahan'
        verbose_name_plural = "Pesanan Tambahan"