from django.db import models

class CVData(models.Model):
    # Data Pribadi
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    nomor_hp = models.CharField(max_length=15)
    alamat = models.TextField()
    
    # Pendidikan
    pendidikan = models.TextField()
    
    # Pengalaman Kerja
    pengalaman = models.TextField()
    
    # Keterampilan
    keterampilan = models.TextField()
    
    # Sertifikasi (opsional)
    sertifikasi = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nama