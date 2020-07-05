from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=50)
    preview=models.TextField()
    describtion=models.TextField()
    photo=models.ImageField(upload_to='image',null=True)
    p1=models.ImageField(upload_to='image',null=True)
    p2=models.ImageField(upload_to='image',null=True)
    p3=models.ImageField(upload_to='image',null=True)
    p4=models.ImageField(upload_to='image',null=True)
    price=models.FloatField()
    offer=models.FloatField()
    # date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def discount (self):
        return self.price * self.offer

    # def new_price (self):
    #     return self.price - self.discount
# Create your models here.


