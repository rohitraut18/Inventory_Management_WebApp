from django.db import models

# Create your models here.

class Inventory(models.Model):  
    ename = models.CharField(max_length=100)
    edescription = models.TextField(max_length=100)  
    edate = models.DateField()
    eavalue = models.CharField(max_length=10)  
    eivalue = models.CharField(max_length=10)  
    ephoto = models.ImageField(upload_to='images')  

    class Meta:  
        db_table = "inventory"  




