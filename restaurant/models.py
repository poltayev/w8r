from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Restaurant(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    logo_path = models.CharField(max_length=250)
    is_deleted = models.SmallIntegerField(default=0)

class Branch(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    is_deleted = models.SmallIntegerField(default=0)

class Waiter(BaseModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    is_deleted = models.SmallIntegerField(default=0)

class Table(BaseModel):
    table_number = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    is_reserved = models.SmallIntegerField(default=0)
    reserved_id = models.CharField(max_length=30)
    updated_by = models.IntegerField()
    is_deleted = models.SmallIntegerField(default=0)

class Menu(BaseModel):
    name = models.CharField(max_length=250)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    is_deleted = models.SmallIntegerField(default=0)
    updated_by = models.IntegerField()

class MenuPosition(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    is_available = models.SmallIntegerField(default=0)
    is_deleted = models.SmallIntegerField(default=0)
    updated_by = models.IntegerField()

class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

class BranchIngredients(BaseModel):
    menu_positions = models.ManyToManyField(MenuPosition)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    is_available = models.SmallIntegerField(default=1)
    is_deleted = models.SmallIntegerField(default=0)

class PaymentType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=20)
    is_disabled = models.SmallIntegerField(default=0)

class OrderStatus(models.Model):
    status_type = models.CharField(max_length=30)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    is_deleted = models.SmallIntegerField(default=0)

class Order(BaseModel):
    NEW = 'new'

    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    waiter = models.ForeignKey(Waiter, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)

class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    menu_position = models.ForeignKey(MenuPosition, on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    unit_discount = models.DecimalField(max_digits=9, decimal_places=2)
    total_unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    is_available = models.SmallIntegerField(default=0)
    is_deleted = models.SmallIntegerField(default=0)





