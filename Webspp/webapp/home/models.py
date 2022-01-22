from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    
    class Meta: 
        db_table = "Category"  
    def __str__(self):
        return str(self.category_name)

class SubCategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta: 
        db_table = "Subcategory"  
    def __str__(self):
        return str(self.subcategory_name)

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    subcategory_id=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=50)
    product_description=models.TextField(max_length=150)
    product_image=models.ImageField()
    color=models.CharField(max_length=10)
    size=models.CharField(max_length=5)
    price=models.DecimalField(decimal_places=2,max_digits=5)
    sku_id=models.CharField(max_length=10)
    is_trending=models.BooleanField(default=0)
    class Meta:
        db_table = "Product"
    def __str__(self):
        return str(self.product_name)