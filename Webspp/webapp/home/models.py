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