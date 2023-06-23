from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.html import mark_safe

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='images/logos/', default=None)
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe(f'<img src="{self.logo.url}" width="150"/>')

    image_tag.short_description = 'Image preview'
    
    class Meta:
        ordering = ['name']

class Branch(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

    class Meta:
        ordering = ['restaurant']

class Waiter(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        ordering = ['surname']

class Table(models.Model):
    table_number = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    is_reserved = models.SmallIntegerField(default=0)
    reserved = models.CharField(max_length=30)
    updated_by = models.IntegerField()
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.table_number

class MenuCategory(models.Model):
    name = models.CharField(max_length=250)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    is_deleted = models.SmallIntegerField(default=0)
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Menu categories"

class MenuPosition(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default=slugify(name))
    description = models.CharField(max_length=500)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    weight = models.DecimalField(max_digits=9, decimal_places=2)
    weight_unit = models.CharField(max_length=10)
    is_available = models.SmallIntegerField(default=0)
    is_deleted = models.SmallIntegerField(default=0)
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

class BranchIngredient(models.Model):
    menu_positions = models.ManyToManyField(MenuPosition)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    is_available = models.SmallIntegerField(default=1)
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    waiter = models.ForeignKey(Waiter, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    menu_position = models.ForeignKey(MenuPosition, on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    unit_discount = models.DecimalField(max_digits=9, decimal_places=2)
    total_unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    is_available = models.SmallIntegerField(default=0)
    is_deleted = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




