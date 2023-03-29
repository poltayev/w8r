from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(BaseModel):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    is_deleted = models.SmallIntegerField(default=0)

class Restaurant(BaseModel):
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    is_deleted = models.SmallIntegerField(default=0)

class Waiter(BaseModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    is_deleted = models.SmallIntegerField(default=0)

class Table(BaseModel):
    table_number = models.IntegerField()
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    is_reserved = models.SmallIntegerField(default=0)
    updated_by = models.IntegerField()
    is_deleted = models.SmallIntegerField(default=0)

class Menu(BaseModel):
    name = models.CharField(max_length=250)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    is_deleted = models.SmallIntegerField(default=0)
    updated_by = models.IntegerField()

class MenuPosition(BaseModel):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    menu_id = models.ForeignKey(Menu, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    is_available = models.SmallIntegerField(default=0)
    is_deleted = models.SmallIntegerField(default=0)
    updated_by = models.IntegerField()

class Ingredient(BaseModel):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    menu_positions = models.ManyToManyField(MenuPosition)

class Order(BaseModel):
    NEW = 'new'
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    table_id = models.ForeignKey(Table, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    waiter_id = models.ForeignKey(Waiter, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    status_type = models.CharField(max_length=30, default=NEW)

class OrderItem(BaseModel):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    menu_position_id = models.ForeignKey(MenuPosition, on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    total_unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    is_available = models.SmallIntegerField(default=0)
    is_deleted = models.SmallIntegerField(default=0)

class OrderStatus(models.Model):
    status_type = models.CharField(max_length=30)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    is_deleted = models.SmallIntegerField(default=0)

class PaymentType(models.Model):
    name = models.CharField(max_length=2)
    type = models.CharField(max_length=50)
    is_deleted = models.SmallIntegerField(default=0)





