from django.db import models
from django.contrib.auth.models import AbstractBaseUser 
from django.core.validators import FileExtensionValidator


class Student(models.Model):
    username=models.CharField(max_length=50, unique=True)
    phone=models.CharField(max_length=100, unique=True)
    email=models.CharField(unique=True , max_length= 50)
    name=models.CharField(max_length=60)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
        # 'Other' option can be added here if needed
    ))
    school=models.CharField(max_length=100)
    date=models.DateField()
    result = models.ImageField(upload_to='result/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png','pdf'])])
    upload = models.CharField(max_length=50,null=False, choices=(
        ('A', 'Adhar Card'),
        ('P', 'Password'),
        ('D', 'Driving License'),
    ))
    documents = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg', 'jpeg', 'png'])])

    def __str__(self):
        return self.username

class Product(models.Model):
    Product_name=models.CharField(max_length=60)
    MRP = models.IntegerField(default=0)
    Price = models.IntegerField(default=0)
    Product_Image = models.ImageField(upload_to='Product_mage/',default="", validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png','pdf'])])

    def __str__(self):
        return self.Product_name
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()
        
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'