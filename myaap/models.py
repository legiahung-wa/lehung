from django.contrib.auth.models import User
from django.db import models 

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=10, blank=True)
    age = models.IntegerField( default= 0,blank= True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="staff", null = True, blank = True)
    address = models.CharField(max_length=200, blank = True, null = True)
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGender(self):
        return self.gender
    def getBirthday(self):
        return self.birthday
    def getImage(self):
        return self.image
    def getAddress(self):
        return self.address


    
 
class Product(models.Model):
    name = models.CharField(max_length = 20, blank=True)  
    image = models.ImageField(upload_to='product', null=True, blank=True)
    price = models.DecimalField(decimal_places = 2, max_digits = 10, blank = True)  
    description = models.TextField(max_length= 200, blank=True, null = True)
    quantity = models.IntegerField(default=0, null=False, blank=False)
    def getName(self):
        return self.name
    def getImage(self):
        return self.image
    def getPrice(self):
        return self.price
    def getDesciption(self):
        return self.description
    def getQuantity(self):
        return self.quantity    
    
