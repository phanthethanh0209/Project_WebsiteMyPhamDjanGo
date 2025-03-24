from django.db import models

# Create your models here.
class NhaCungCap(models.Model):
    MaNCC = models.CharField(primary_key=True, max_length=20)
    TenNCC = models.CharField(max_length=255)
    DiaChi = models.TextField()
    SDT = models.CharField(max_length=11)
    Email = models.TextField()
    Website = models.TextField()

class LoaiSanPhan(models.Model):
    MaLoai = models.CharField(primary_key=True, max_length=20)
    TenLoai = models.CharField(max_length=255)

    MaNCC = models.ForeignKey(NhaCungCap, on_delete=models.RESTRICT, null=True)

class ThuongHieu(models.Model):
    MaTH = models.CharField(primary_key=True, max_length=20)
    TenTH = models.CharField(max_length=255)

    MaNCC = models.ForeignKey(NhaCungCap, on_delete=models.RESTRICT, null=True)

class SanPham(models.Model):
    MaSP = models.CharField(primary_key=True, max_length=20)
    TenSP = models.CharField(max_length=255)
    HinhAnh = models.TextField()
    NSX = models.DateTimeField()
    HSD = models.DateTimeField()
    MoTa = models.TextField()
    GiaBan = models.DecimalField(max_digits=10, decimal_places=2) #decimal_places xác định số chữ số thập phân sau dấu chấm thập phân.
    SoLuongTon = models.IntegerField()
    TrongLuong = models.DecimalField(max_digits=10, decimal_places=2)

    MaLoai = models.ForeignKey(LoaiSanPhan, on_delete=models.RESTRICT, null=True)
    MaTH = models.ForeignKey(ThuongHieu, on_delete=models.RESTRICT, null=True)


class TaiKhoan(models.Model):
    TenTK = models.CharField(primary_key=True, max_length=20)
    MatKhau = models.CharField(max_length=32)
    Email = models.TextField()
    VaiTro = models.TextField()

class NhanVien(models.Model):
    MaNV = models.CharField(primary_key=True, max_length=20)
    TenNV = models.CharField(max_length=32)
    DiaChi = models.TextField()
    SDT = models.CharField(max_length=11)
    Email = models.TextField()
    ChucVu = models.TextField()

    TenTK = models.ForeignKey(TaiKhoan, on_delete=models.RESTRICT, null=True)

class ThongTinKhachHang(models.Model):
    MaKH = models.CharField(primary_key=True, max_length=20)
    HoTen = models.TextField()
    SDT = models.CharField(max_length=11)
    DiaChi = models.TextField()
    
    TenTK = models.ForeignKey(TaiKhoan, on_delete=models.RESTRICT, null=True)


class PhieuNhapHang(models.Model):
    MaPNH = models.CharField(primary_key=True, max_length=20)
    NgayNhap = models.DateTimeField(auto_now_add=True)
    TongTien = models.DecimalField(max_digits=10, decimal_places=2)
    
    MaNCC = models.ForeignKey(NhaCungCap, on_delete=models.RESTRICT, null=True)
    TenTK = models.ForeignKey(TaiKhoan, on_delete=models.RESTRICT, null=True)

class CTPhieuNhapHang(models.Model):
    MaSP = models.ForeignKey(SanPham, on_delete=models.RESTRICT)
    MaPNH = models.ForeignKey(PhieuNhapHang, on_delete=models.RESTRICT)
    SoLuong = models.IntegerField()
    DonGia = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        # Định nghĩa hai trường foreign key làm khóa chính
        unique_together = ('MaSP', 'MaPNH')


class KhuyenMai(models.Model):
    MaKM = models.CharField(primary_key=True, max_length=20)
    TenKM = models.CharField(max_length=32)
    GiaGiam = models.DecimalField(max_digits=10, decimal_places=2)


class CTKhuyenMai(models.Model):
    MaKM = models.ForeignKey(KhuyenMai, on_delete=models.RESTRICT)
    MaSP = models.ForeignKey(SanPham, on_delete=models.RESTRICT)
    NgayBD = models.DateTimeField()
    NgayKT = models.DateTimeField()

    class Meta:
        # Định nghĩa hai trường foreign key làm khóa chính
        unique_together = ('MaKM', 'MaSP')

class CTGioHang(models.Model):
    MaSP = models.ForeignKey(SanPham, on_delete=models.RESTRICT)
    TenTK = models.ForeignKey(TaiKhoan, on_delete=models.RESTRICT)
    SoLuong = models.IntegerField()
    DonGia = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        # Định nghĩa hai trường foreign key làm khóa chính
        unique_together = ('MaSP', 'TenTK')


class HoaDon(models.Model):
    MaHD = models.CharField(primary_key=True, max_length=20)
    NgayLap = models.DateTimeField(auto_now_add=True)
    TongTien = models.DecimalField(max_digits=10, decimal_places=2) #decimal_places xác định số chữ số thập phân sau dấu chấm thập phân.
    TrangThai = models.IntegerField()
    PhuongThucThanhToan = models.TextField()
    DiaChiGiaoHang = models.TextField()
    TenKhachHang = models.TextField()
    SDT = models.CharField(max_length=11)
    
    TenTK = models.ForeignKey(TaiKhoan, on_delete=models.RESTRICT, null=True)


class CTHoaDon(models.Model):
    MaSP = models.ForeignKey(SanPham, on_delete=models.RESTRICT)
    MaHD = models.ForeignKey(HoaDon, on_delete=models.RESTRICT)
    SoLuong = models.IntegerField(default=1)
    DonGia = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        # Định nghĩa hai trường foreign key làm khóa chính
        unique_together = ('MaSP', 'MaHD')


class DanhGia(models.Model):
    CTHoaDon = models.ForeignKey(CTHoaDon, on_delete=models.RESTRICT)
    NoiDung = models.TextField()
    NgayDanhGia = models.DateTimeField(auto_now_add=True)
    SoSao = models.IntegerField()

