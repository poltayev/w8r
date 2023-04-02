from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    logo_path = models.CharField(max_length=250)
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Branch(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['restaurant_id'])
        ]

class Waiter(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['branch_id'])
        ]

class Table(models.Model):
    table_number = models.IntegerField()
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    is_reserved = models.SmallIntegerField(default=0)
    reserved_id = models.CharField(max_length=30)
    updated_by = models.IntegerField()
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['branch_id'])
        ]

class Menu(models.Model):
    name = models.CharField(max_length=250)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    is_deleted = models.SmallIntegerField(default=0)
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['branch_id'])
        ]

class MenuPosition(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default=slugify(name))
    description = models.CharField(max_length=250)
    menu_id = models.ForeignKey(Menu, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    is_available = models.SmallIntegerField(default=0)
    is_deleted = models.SmallIntegerField(default=0)
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['menu_id'])
        ]

class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

class BranchIngredient(models.Model):
    menu_positions = models.ManyToManyField(MenuPosition)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    is_available = models.SmallIntegerField(default=1)
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['ingredient_id'])
        ]

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

class Order(models.Model):
    NEW = 'new'

    branch_id = models.ForeignKey(Branch, on_delete=models.PROTECT)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    table_id = models.ForeignKey(Table, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    waiter_id = models.ForeignKey(Waiter, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['branch_id'])
        ]

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    menu_position_id = models.ForeignKey(MenuPosition, on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    unit_discount = models.DecimalField(max_digits=9, decimal_places=2)
    total_unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    is_available = models.SmallIntegerField(default=0)
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['order_id'])
        ]





