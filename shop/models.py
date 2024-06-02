from django.db import models

# Create your models here.
class Product(models.Model):
    
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category =models.CharField(max_length =50, default='')
    subcategory = models.CharField(max_length=50, default='')
    price =models.IntegerField(default=100)
    pub_date = models.DateField()
    desc=models.CharField(max_length=300)
    image = models.ImageField(upload_to="shop/images/", default='')


    