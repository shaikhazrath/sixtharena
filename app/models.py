from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

STATE_CHOICES = {
('andhra pradesh', 'andhra pradesh'),
}


class Customer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	locality = models.CharField(max_length=200)
	city = models.CharField(max_length=50)
	zipcode = models.IntegerField()
	state = models.CharField(choices=STATE_CHOICES, max_length=50)
	phoneNumber = models.PositiveIntegerField()

	def __str__(self):
		return str(self.id)


CATEGORY_CHOICES = {
('TW', 'Topwear'),
('BW', 'Bottomwear'),
('SH', 'SHOES'),
('W', '	WATCH')


}


class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    product_img = CloudinaryField('image')
    product_imag = CloudinaryField('image')
    product_image = CloudinaryField('image')
    product_images = CloudinaryField('image')
    def __str__(self):
        return str(self.title)






class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	Size = models.CharField(max_length=200)
	quantity = models.PositiveIntegerField(default=1)
	def __str__(self):
	      return str(self.id)
@property
def total_cost(self):
    	return self.quantity * self.product.discount_price



STATUS_CHOICES = {
('ACCEPTED','ACCEPTED'),
('Packed','Packed'),
('On the Way','On the way'),
('Deliverd','Deliverd'),
('cancel','cancel'),
}
	
class OrderPlaced(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
	product = models.ForeignKey(Product, on_delete= models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	ordered_date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(choices=STATUS_CHOICES, max_length=50,default='Pending')
	@property
	def total_cost(self):
		return self.quantity * self.product.discount_price


class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	message = models.TextField()
	def total_cost(self):
		return message 
