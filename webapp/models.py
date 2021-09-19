from django.db import models

class Products(models.Model):
	Product_id = models.IntegerField()
	Product_name = models.CharField(max_length=100)
	Product_price = models.IntegerField()
	Product_manufacturer = models.CharField(max_length=30)
	Product_image = models.ImageField(null=True,blank=True, upload_to="dbimages/")

class Signup(models.Model):
	Name = models.CharField(max_length=50)
	Mailid = models.CharField(max_length=60)
	Contactnumber = models.BigIntegerField()
	Location = models.CharField(max_length=40)

class Order(models.Model):
	Fullname = models.CharField(max_length=100)
	Location = models.CharField(max_length=20)
	Contactnumber = models.BigIntegerField()
	Emailid = models.CharField(max_length=100)
	Shippingaddress = models.CharField(max_length=400)
	Nearbylandmark = models.CharField(max_length=40)
	







   