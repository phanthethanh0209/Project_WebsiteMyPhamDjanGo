# from django.contrib import admin
# from django.urls import path
# from . import views


# urlpatterns= [

# #---------------------------------------------------------------------------------------------------------------------#
# #--------------------------------------------------------TRANG CỬA HÀNG-----------------------------------------------#
# #---------------------------------------------------------------------------------------------------------------------# 
#     path('', views.index, name='index'),
#     path('news/', views.news, name='news'),
#     path('shop/', views.shop, name='shop'),
#     path('shop_detail/<int:sp_id>/', views.shop_detail, name='shop_detail'),
#     path('contact/', views.contact, name='contact'),
#     path('about/', views.about, name='about'),
#     path('login/', views.login, name='login'),
#     path('signup/', views.signup, name='signup'),
#     path('session_info/', views.session_info, name='session_info'),
#     path('logout/', views.auth_logout, name='auth_logout'),
#     path('cart/', views.cart, name='cart'),
#     path('shop_theoloai/<int:ml>/', views.DSSPTheoLoai, name='DSSPTheoLoai'),
#     path('shop_ThuongHieu/<int:ml>/', views.DSSPTheoTH, name='DSSPTheoTH'),
#     path('checkout/', views.checkout, name='checkout'),
#     path('order_details/', views.order_user, name='order_details'),



# #----------------------------------------------------------GIỎ HÀNG---------------------------------------------------#   
#     path('cart/', views.cart, name='cart'),
#     path('addCart/', views.addProToCart, name='addCart'),
#     path('clearCart/', views.clearCart, name='clearCart'),
#     path('deleteOnePro/<int:product_id>/', views.deleteProFromCart, name='deleteOnePro'),
#     path('increase_quantity/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
#     path('decrease_quantity/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),



# #---------------------------------------------------------------------------------------------------------------------#
# #--------------------------------------------------------TRANG ADMIN--------------------------------------------------#
# #---------------------------------------------------------------------------------------------------------------------# 



# #--------------------------------------TRANG CHỦ ADMIN--------------------------------------------#
#     path('admin/', views.indexAdmin, name='index'),

# #--------------------------------------QUẢN LÝ SẢN PHẨM--------------------------------------------#
#     path('admin/products/', views.products, name='products'),
#     path('admin/detail_product/<int:product_id>/', views.detail_product, name='detail_product'),
#     path('admin/add_product/', views.add_product, name='add_product'),#thêm sản phẩm
#     path('admin/edit_product/<int:id_product>/', views.edit_product, name='edit_product'),
#     path('admin/products/<int:id>/delete', views.delete_product, name='delete_product'),#xóa sản phẩm


# #--------------------------------------QUẢN LÝ THƯƠNG HIỆU--------------------------------------------#
#     path('admin/brands/', views.brands, name='brands'),#danh sách thương hiệu
#     path('admin/add_brand/', views.add_brand, name='add_brand'),#thêm thương hiệu
#     path('admin/edit_brand/<int:id_brand>/', views.edit_brand, name='edit_brand'),#sửa thương hiệu
#     path('delete_brand/<int:id_brand>/', views.delete_brand, name='delete_brand'),#xóa thương hiệu

# #--------------------------------------QUẢN LÝ LOẠI HÀNG--------------------------------------------#
#     path('admin/categorys/', views.categorys, name='categorys'),#danh sách loại hàng
#     path('admin/detail_category/<int:id_category>/', views.detail_category, name='detail_category'),#xem chi tiết loại hàng
#     path('admin/add_category/', views.add_category, name='add_category'),#thêm loại hàng
#     path('admin/edit_category/<int:id_category>/', views.edit_category, name='edit_category'),#sửa loại hàng
#     path('admin/categorys/<int:id_category>/delete', views.delete_category, name='delete_category'),#xóa loại hàng

# #--------------------------------------QUẢN LÝ ĐƠN HÀNG--------------------------------------------#
#     path('admin/orders/', views.orders, name='orders'), #danh sách đơn hàng
#     path('admin/detail_order/<int:id_order>/', views.detail_order, name='detail_order'), #chi tiết đơn hàng
    
# #--------------------------------------QUẢN LÝ NGƯỜI DÙNG--------------------------------------------#
#     path('admin/users/', views.users, name='users'), #danh sách người dùng
#     path('admin/add_user/', views.add_user, name='add_user'), #thêm người dùng
#     path('admin/users/<int:user_id>/delete', views.delete_user, name='delete_user'),
#     path('admin/edit_user/<int:user_id>/', views.edit_user, name='edit_user'), #sửa người dùng


# ]



# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

# #-------------------------------------------------TRANG ADMIN--------------------------------------------#
    path('admin/', views.trangChuAdmin, name='trangChuAdmin'),   

# #-------------------------------------------------XEM THÔNG ITN KHÁCH HÀNG--------------------------------------------#
    #path('xemThongTinKhachHang/', views.xemThongTinKhachHang, name='xemThongTinKhachHang'),
    path('xemThongTinKhachHang/', views.xemThongTinCua1NguoiDung, name='xemThongTinKhachHang'),
    path('themThongTinKH/', views.themThongTinKhachHang, name='themTTKH'),
    path('capNhatThongTinKH/', views.capNhatThongTinKhachHang, name='capNhatTTKH'),
    path('xoaThongTinKH/', views.xoaThongTinKhachHang, name='xoaTTKH'),
    path('capNhatTaiKhoan/', views.capNhatTaiKhoan, name='capNhatTK'),

# #-------------------------------------------------QUẢN LÝ KHUYẾN MÃI--------------------------------------------#
    path('admin/themKhuyenMai', views.themKhuyenMai, name='themKhuyenMai'),  # Thay `home` bằng view cụ thể của bạn
    path('admin/khuyenMai/', views.khuyenMai, name='khuyenMai'),  # Thay `home` bằng view cụ thể của bạn
    path('admin/suaKhuyenMai/<str:makm>', views.suaKhuyenMai, name='suaKhuyenMai'),  # Thay `home` bằng view cụ thể của bạn
    path('admin/xoaKhuyenMai/<str:makm>', views.xoaKhuyenMai, name='xoaKhuyenMai'),  # Thay `home` bằng view cụ thể của bạn
    path('admin/CTKhuyenMai/<str:makm>/', views.chiTietKhuyenMai, name='CTKhuyenMai'),  # Thay `home` bằng view cụ thể của bạn
    path('admin/themCTKM/<str:makm>', views.themSPVaoKhuyenMai, name='themCTKM'),  # Thay `home` bằng view cụ thể của bạn
    path('admin/get_available_products/<str:start_date>/<str:end_date>/', views.get_available_products, name='get_available_products'),
    path('admin/xoaCTKM/<str:makm>/<str:masp>/', views.xoaCTKhuyenMai, name='xoaCTKhuyenMai'),
    path('admin/suaCTKM/<str:makm>/<str:masp>/', views.suaCTKhuyenMai, name='suaCTKhuyenMai'),

# #--------------------------------------QUẢN LÝ NGƯỜI DÙNG--------------------------------------------#
    path('admin/themTaiKhoan/', views.themTaiKhoan, name='themTaiKhoan'),
    path('admin/suaTaiKhoan/<str:tenTaiKhoan>/', views.suaTaiKhoan, name='suaTaiKhoan'),
    path('admin/xoaTaiKhoan/<str:tenTaiKhoan>/', views.xoaTaiKhoan, name='xoaTaiKhoan'),
    path('admin/danhSachTaiKhoan/', views.xemDanhSachTaiKhoan, name='danhSachTaiKhoan'),
    path('admin/capTaiKhoan/<str:maNhanVien>/', views.capTaiKhoan, name='capTaiKhoan'),

# #--------------------------------------QUẢN LÝ NHÂN VIÊN--------------------------------------------#
    path('admin/danhSachNhanVien/', views.xemDanhSachNhanVien, name='danhSachNhanVien'),
    path('admin/themNhanVien/', views.themNhanVien, name='themNhanVien'),
    path('admin/suaNhanVien/<str:maNhanVien>/', views.suaNhanVien, name='suaNhanVien'),
    path('admin/xoaNhanVien/<str:maNhanVien>/', views.xoaNhanVien, name='xoaNhanVien'),
    path('admin/xemChiTietNhanVien/<str:maNhanVien>/', views.xemChiTietNhanVien, name='xemChiTietNhanVien'),

# #--------------------------------------QUẢN LÝ LOẠI SẢN PHẨM--------------------------------------------#
    path('admin/themLoaiSP/', views.themLoaiSP, name='themLoaiSP'),
    path('admin/suaLoaiSP/<str:maloai>/', views.suaLoaiSP, name='suaLoaiSP'),
    path('admin/xoaLoaiSP/<str:malsp>/', views.xoaLoaiSP, name='xoaLoaiSP'),
    path('admin/danhSachLoaiSP/', views.danhSachLoaiSP, name='danhSachLoaiSP'),

# #--------------------------------------QUẢN LÝ THƯƠNG HIỆU--------------------------------------------#
    path('admin/themTH/', views.themTH, name='themTH'),
    path('admin/suaTH/<str:mathuonghieu>/', views.suaTH, name='suaTH'),
    path('admin/xoaTH/<str:math>/', views.xoaTH, name='xoaTH'),
    path('admin/danhSachTH/', views.danhSachTH, name='danhSachTH'),

# #--------------------------------------QUẢN LÝ NHÀ CUNG CẤP--------------------------------------------#
    path('admin/themNhaCungCap/', views.themNhaCungCap, name='themNhaCungCap'),
    path('admin/suaNhaCungCap/<str:maNCC>/', views.suaNhaCungCap, name='suaNhaCungCap'),
    path('admin/xoaNhaCungCap/<str:mancc>/', views.xoaNhaCungCap, name='xoaNhaCungCap'),
    path('admin/danhSachNhaCungCap/', views.danhSachNhaCungCap, name='danhSachNhaCungCap'),

# #--------------------------------------QUẢN LÝ SẢN PHẨM------------------------------------------------#
    path('admin/danhSachSanPham/', views.danhSachSanPham, name='danhSachSanPham'),
    # path('admin/danhSachSanPham/', views.xemChiTietCua1SanPham, name='danhSachSanPham'),
    path('admin/themSP/', views.themSP, name='themSP'),
    path('admin/suaSP/<str:masanpham>/', views.suaSP, name='suaSP'),
    path('admin/xoaSP/<str:masp>/', views.xoaSP, name='xoaSP'),
    path('admin/xemCT/<str:MaSP>/', views.xemChiTietSP, name='xemCT'),

# #-------------------------------------------------THANH TOÁN--------------------------------------------#
    path('checkout/', views.checkout, name='checkout'),
    path('pay/', views.index_payment, name='pay'),
    path('payment/', views.payment, name='payment'),
    path('payment_ipn/', views.payment_ipn, name='payment_ipn'),
    path('payment_return/', views.payment_return, name='payment_return'),
    path('query/', views.query, name='query'),
    path('refund/', views.refund, name='refund'),
    path('lichSuMuaHang/', views.xemlichSuMuaHang, name='lichSuMuaHang'),
    # path('admin/', admin.site.urls),

#--------------------------------------------------TRANG CHỦ--------------------------------------------#
    path('', views.index, name='index'),
    path('shop/', views.xemTatCaSanPham, name='shop'),
    path('shop_theoloai/<str:MaLoai>/', views.xemTatCaSanPhamTheoLoai, name='shop_theoloai'),
    path('shop_ThuongHieu/<str:MaTH>/', views.xemTatCaSanPhamTheoThuongHieu, name='shop_ThuongHieu'),
    path('shop_detail/<str:MaSP>', views.xemChiTietCua1SanPham, name='shop_detail'),  #xem chi tiết sản phẩm và đánh giá
    path('dangKyTaiKhoan/', views.dangKyTaiKhoan, name='dangKy'),
    path('dangNhap/', views.dangNhap, name='dangNhap'),
    path('dangXuat/', views.dangXuat, name='dangXuat'),


#----------------------------------------------GIỎ HÀNG--------------------------------------------#
    path('cart/', views.cart, name='cart'),
    path('addCart/', views.addProToCart, name='addCart'),
    path('deleteOnePro/<slug:product_id>/', views.deleteProFromCart, name='deleteOnePro'),
    path('clearCart/', views.clearCart, name='clearCart'),
    path('increase_quantity/<str:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<str:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    
#-------------------------------------------ĐÁNH GIÁ SẢN PHẨM--------------------------------------------#
    path('shop_detail/danhGia/<str:MaSP>', views.danhGiaMotSanPham, name='danhGiaSanPham'),
    

    # path('customer_info/', views.xemThongTinKhachHang, name='xemThongTinKhachHang')


     #Quản lý nhập hàng
    path('admin/danhSachNhapHang/', views.danhSachNhapHang, name='danhSachNhapHang'),
    path('admin/themNhapHang/', views.themNhapHang, name='themNhapHang'),
    path('admin/xoaNhapHang/<str:maPNH>/', views.xoaNhapHang, name='xoaNhapHang'),
    path('admin/suaNhapHang/<str:maPNH>/', views.suaNhapHang, name='suaNhapHang'),

    path('admin/XemCTNhapHang/<str:maPNH>/', views.XemCTNhapHang, name='XemCTNhapHang'),

    path('admin/LichSuDonHang/', views.LichSuDonHang, name='LichSuDonHang'),
    path('admin/XemCTDonHang/<str:MaHD>/', views.XemCTDonHang, name='XemCTDonHang'),


#-------------------------------------------THỐNG KÊ & BÁO CÁO--------------------------------------------#
    path('admin/thongKeDoanhThu/', views.thongKeDoanhThu, name='thongKeDoanhThu'),
    path('admin/thongKeSanPham/', views.thongKeSanPham, name='thongKeSanPham'),
    path('admin/thongKeDonHang/', views.thongKeDonHang, name='thongKeDonHang'),

    # Xuất báo cáo Excel
    path('admin/thongKeDoanhThu/export/', views.export_doanh_thu_excel, name='export_doanh_thu_excel'),
    path('admin/thongKeSanPham/export/', views.export_san_pham_excel, name='export_san_pham_excel'),
    path('admin/thongKeDonHang/export/', views.export_don_hang_excel, name='export_don_hang_excel'),
]