from django.db import models

# Create your models here.
class Gioi_tinh(models.Model):
    ten_gioitinh  = models.CharField(max_length=5)

    def __str__(self):
        return str(self.ten_gioitinh)
    
class Nhan_vien(models.Model):
    cccd = models.CharField(max_length=20, unique=True)
    ten_nhanvien = models.CharField(max_length=5)
    ten_gioitinh = models.ForeignKey(Gioi_tinh, on_delete=models.CASCADE)
    dien_thoai = models.CharField(unique=True)
    dia_chi = models.CharField(max_length=100)

    def __str__(self):
        return str(self.cccd) + '-' + str(self.dien_thoai)
    