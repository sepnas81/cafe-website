from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.username


class Admin(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    sugar = models.IntegerField()
    coffee = models.IntegerField()
    flour = models.IntegerField()
    chocolate = models.IntegerField()
    egg = models.IntegerField()
    vertical = models.BinaryField(max_length=1)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_amount = models.IntegerField()
    type = models.BinaryField(max_length=1)

    def __str__(self):
        return str(self.order_id)


class OrdersProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order {self.order.order_id} - Product {self.product.name}'


class UsersOrders(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order {self.order.order_id} - Product {self.user.username}'


class Storage(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()

    def __str__(self):
        return self.name
