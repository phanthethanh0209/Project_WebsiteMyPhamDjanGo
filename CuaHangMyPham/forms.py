# import re
# from django import forms
# from .models import Category, Brand, User,Product, Order, OrderDetail
# #import re 
# # from django.contrib.auth.models import User

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name']

#     def __init__(self, *args, **kwargs):
#         super(CategoryForm, self).__init__(*args, **kwargs)
#         self.fields['name'].error_messages = {'required': 'Tên không được để trống'}

#     def clean_name(self):
#         name = self.cleaned_data.get('name')
#         if Category.objects.filter(name=name).exists():
#             raise forms.ValidationError("Loại đã tồn tại")
#         return name
    

# class BrandForm(forms.ModelForm):
#     class Meta:
#         model = Brand
#         fields = ['name']
#         error_messages = {
#             'name': {
#                 'required': "Tên thương hiệu không được để trống",
#             },
#         }

#     # *args là một tuple chứa các đối số không đặt tên.
#     # **kwargs là một từ điển chứa các đối số từ khóa.
#     def __init__(self, *args, **kwargs):
#         # lấy giá trị của khóa 'instance' từ kwargs nếu có, nếu không thì trả về None.
#         self.instance = kwargs.get('instance', None)
#         super(BrandForm, self).__init__(*args, **kwargs)

# # Phương thức này sẽ tự động được gọi khi gọi is_valid() trên form
#     def clean_name(self):
#         name = self.cleaned_data.get('name')
        
#         if not name:
#             raise forms.ValidationError("Tên thương hiệu không được để trống")
#         # exclude(pk=self.instance.pk): Loại trừ đối tượng hiện tại (nếu đang chỉnh sửa) ra khỏi danh sách kiểm tra. tức là loại bỏ các đối tượng có pk = pk trong csdl
#         if Brand.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
#             raise forms.ValidationError("Thương hiệu đã tồn tại")
#         return name

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['recipient_name', 'recipient_address', 'recipient_phone', 'method_payment']
        
#     def __init__(self, *args, **kwargs):
#         super(OrderForm, self).__init__(*args, **kwargs)
#         self.fields['recipient_name'].error_messages = {'required': 'Tên không được để trống'}
#         self.fields['recipient_address'].error_messages = {'required': 'Địa chỉ không được để trống'}
#         self.fields['recipient_phone'].error_messages = {'required': 'Số điện thoại không được để trống'}
#         self.fields['method_payment'].error_messages = {'required': 'Phương thức thanh toán không được để trống'}

#     def clean_recipient_phone(self):
#         recipient_phone = self.cleaned_data.get('recipient_phone')
#         if not recipient_phone:
#             raise forms.ValidationError("Số điện thoại không được để trống")
#         if not recipient_phone.isdigit() or not re.match(r"^0\d{9}$", recipient_phone) or len(recipient_phone) > 10:
#             raise forms.ValidationError("Số điện thoại không hợp lệ!")
#         return recipient_phone

# class OrderDetailForm(forms.ModelForm):
#     class Meta:
#         model = OrderDetail
#         fields = ['product', 'quantity']

# class UpdateOrderStatusForm(forms.Form):
#     status = forms.CharField(max_length=100)
    
    
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'email', 'phone', 'password', 'role']

#     def __init__(self, *args, **kwargs):
#         super(UserForm, self).__init__(*args, **kwargs)
#         self.fields['name'].error_messages = {'required': 'Tên không được để trống'}
#         self.fields['email'].error_messages = {'required': 'Email không được để trống'}
#         self.fields['phone'].error_messages = {'required': 'Số điện thoại không được để trống'}
#         self.fields['password'].error_messages = {'required': 'Mật khẩu không được để trống'}
#         self.fields['role'].error_messages = {'required': 'Vai trò không được để trống'}

#     def clean_name(self):
#         name = self.cleaned_data.get('name')
#         if not name:
#             raise forms.ValidationError("Tên không được để trống")
#         return name

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not email:
#             raise forms.ValidationError("Email không được để trống")
#         if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             raise forms.ValidationError("Email không hợp lệ")
#         return email

#     def clean_phone(self):
#         phone = self.cleaned_data.get('phone')
#         if not phone:
#             raise forms.ValidationError("Số điện thoại không được để trống")
#         if not re.match(r"0[0-9]{9}", phone):
#             raise forms.ValidationError("Số điện thoại không hợp lệ")
#         return phone

#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if not password:
#             raise forms.ValidationError("Mật khẩu không được để trống")
#         if len(password) < 8:
#             raise forms.ValidationError("Mật khẩu phải có ít nhất 8 ký tự")
#         if not re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password):
#             raise forms.ValidationError('Mật khẩu phải chứa ít nhất một chữ cái và một số')
#         return password

#     def clean_role(self):
#         role = self.cleaned_data.get('role')
#         if not role:
#             raise forms.ValidationError("Vai trò không được để trống")
#         return role
    

# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def __init__(self, *args, **kwargs):
#         super(LoginForm, self).__init__(*args, **kwargs)
#         self.fields['email'].error_messages = {'required': 'Email không được để trống'}
#         self.fields['password'].error_messages = {'required': 'Mật khẩu không được để trống'}

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not email:
#             raise forms.ValidationError("Email không được để trống")
#         if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             raise forms.ValidationError("Email không hợp lệ")
#         return email
    
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if not password:
#             raise forms.ValidationError("Mật khẩu không được để trống")
#         if len(password) < 8:
#             raise forms.ValidationError("Mật khẩu phải có ít nhất 8 ký tự")
#         if not re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password):
#             raise forms.ValidationError('Mật khẩu phải chứa ít nhất một chữ cái và một số')
#         return password
    
    
# class SignUpForm(forms.ModelForm):
#     confirm_password = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Nhập lại mật khẩu không được để trống'})

#     class Meta:
#         model = User
#         fields = ['name', 'email', 'phone', 'password']

#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)
#         self.fields['name'].error_messages = {'required': 'Tên không được để trống'}
#         self.fields['email'].error_messages = {'required': 'Email không được để trống'}
#         self.fields['phone'].error_messages = {'required': 'Số điện thoại không được để trống'}
#         self.fields['password'].error_messages = {'required': 'Mật khẩu không được để trống'}

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not email:
#             raise forms.ValidationError("Email không được để trống")
#         if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             raise forms.ValidationError("Email không hợp lệ")
#         return email

#     def clean_phone(self):
#         phone = self.cleaned_data.get('phone')
#         if not phone:
#             raise forms.ValidationError("Số điện thoại không được để trống")
#         if not re.match(r"0[0-9]{9}", phone):
#             raise forms.ValidationError("Số điện thoại không hợp lệ")
#         return phone

#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if not password:
#             raise forms.ValidationError("Mật khẩu không được để trống")
#         if len(password) < 8:
#             raise forms.ValidationError("Mật khẩu phải có ít nhất 8 ký tự")
#         if not re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password):
#             raise forms.ValidationError('Mật khẩu phải chứa ít nhất một chữ cái và một số')
#         return password

#     def clean_confirm_password(self):
#         confirm_password = self.cleaned_data.get('confirm_password')
#         password = self.cleaned_data.get('password')
#         if confirm_password != password:
#             raise forms.ValidationError("Mật khẩu không khớp")
#         return confirm_password
        
    
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['category', 'brand', 'name', 'price', 'description', 'image']


    
#     def __init__(self, *args, **kwargs):
#         super(ProductForm, self).__init__(*args, **kwargs)
#         self.fields['category'].error_messages = {'required': 'Loại không được để trống'}
#         self.fields['brand'].error_messages = {'required': 'Thương hiệu không được để trống'}
#         self.fields['name'].error_messages = {'required': 'Tên sản phẩm không được để trống'}
#         self.fields['price'].error_messages = {'required': 'Giá không được để trống'}
#         self.fields['description'].error_messages = {'required': 'Mô tả khẩu không được để trống'}
#         self.fields['image'].error_messages = {'required': 'Hình không được để trống'}

#     def clean_name(self):
#         name = self.cleaned_data['name']
#         return name


from django import forms


class PaymentForm(forms.Form):

    order_id = forms.CharField(max_length=250)
    order_type = forms.CharField(max_length=20)
    amount = forms.IntegerField()
    order_desc = forms.CharField(max_length=100)
    bank_code = forms.CharField(max_length=20, required=False)
    language = forms.CharField(max_length=2)
