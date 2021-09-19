from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

# Create your models here.

################
#1 Product ++
#2 CartProduct ++
#3 Cart ++
#4 Order
################

#5* Customer
#6* Specifications

class Product(models.Model):
	title = models.CharField(max_length = 255, verbose_name = 'Name')
	slug = models.SlugField(unique = True)
	image = models.ImageField(verbose_name = 'Image')
	description = models.TextField(verbose_name = 'Description', null=True)
	price = models.DecimalField(max_digits = 9, decimal_places = 2, verbose_name = 'Price')

	def __str__(self):
		return self.title


class CartProduct(models.Model):
	user = models.ForeignKey('Customer', verbose_name = 'Customer', on_delete = models.CASCADE)
	cart = models.ForeignKey('Cart', verbose_name = 'Cart', on_delete = models.CASCADE, related_name = '+')
	product = models.ForeignKey(Product, verbose_name = 'Product', on_delete = models.CASCADE)
	qty = models.PositiveIntegerField(default = 1)
	final_price = models.DecimalField(max_digits = 9, decimal_places = 2, verbose_name = 'Totel price')

	def __str__(self):
		return "Cart product: {}".format(self.product.title)


class Cart(models.Model):
	owner = models.ForeignKey('Customer', verbose_name = 'Owner', on_delete = models.CASCADE)
	products = models.ManyToManyField(CartProduct, blank = True)
	total_products = models.PositiveIntegerField(default = 0)
	final_price = models.DecimalField(max_digits = 9, decimal_places = 2, verbose_name = 'Totel price')

	def __str__(self):
		return str(self.id)


class Customer(models.Model):
	user = models.ForeignKey(User, verbose_name = 'User', on_delete = models.CASCADE)
	phone = models.CharField(max_length = 20, verbose_name = 'Phone number')
	address = models.CharField(max_length = 255, verbose_name = 'Address')

	def __str__(self):
		return "Customer: {} {}".format(self.user.first_name, self.user.last_name)

class Specifications(models.Model):
	content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
	object_id = models.PositiveIntegerField()
	name = models.CharField(max_length = 255, verbose_name = 'product name for specifications')

	def __str__(self):
		return "Specifications for product {}".format(self.name)
