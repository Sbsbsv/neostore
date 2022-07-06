from asyncio.windows_events import NULL
from datetime import datetime
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from pickle import TRUE
# from tkinter.messagebox import YES
from django.db import models

rexoptions = (
    ('Yes','Yes'),
    ('No','No'),
    
)

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    product_desc=models.CharField(max_length=1000)
  
    warrenty=models.CharField(max_length=100,default="1 Year",null=True)
    rex = models.CharField(max_length=6, choices=rexoptions, default='Yes')
    date=models.DateField()
    image=models.ImageField(upload_to='images',default="")
    image2=models.ImageField(upload_to='images',default="")
    image3=models.ImageField(upload_to='images',default="")
    image4=models.ImageField(upload_to='images',default="")

    def __str__(self): 
        return self.product_name

class studentImage(models.Model):
    text=models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
         return self.text


class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50)
    query=models.CharField(max_length=1000,default="")
    datetime= models.DateTimeField(auto_now_add= True)

    def __str__(self): 
        y=str(self.datetime)
        x=slice(16)
        reti=self.name+" "+y[x]
        return reti

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50) 
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipc=models.CharField(max_length=50,default=True)
    address=models.CharField(max_length=50)
    item_Json=models.CharField(max_length=5000,default="")
    amount=models.IntegerField(default=0)
    

    def __str__(self): 
        bola=str(self.order_id)
        return bola

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        bola=str(self.order_id)
        return bola

class promocode(models.Model):
    promo=models.CharField(max_length=100,)
    effect=models.IntegerField(default=10)

    def __str__(self):
        return self.promo


