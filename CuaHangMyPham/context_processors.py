# from .models import Category, Brand, Cart

def menu(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT MaLoai, TenLoai
            FROM LoaiSanPhan
        """)
        categories = cursor.fetchall()

        cursor.execute("""
            SELECT MaTH, TenTH
            FROM ThuongHieu
        """)
        brands = cursor.fetchall()
    return {'categories': categories, 'brands': brands}


from django.db import connection

def cart_item_count(request):
    total_item = 0
    tenTaiKhoan = request.session.get('tenTaiKhoan')
    if tenTaiKhoan:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM CTGioHang WHERE TenTK = %s", [tenTaiKhoan])
            row = cursor.fetchone()
            total_item = row[0]
    return {'cart_item_count': total_item}
