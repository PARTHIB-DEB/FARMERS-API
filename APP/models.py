from django.db import models

# Create your models here.

class family(models.Model):
    Farmer=models.CharField(max_length=100)
    Wife=models.CharField(max_length=100)
    children=models.IntegerField(null=True,blank=True)
    cows=models.IntegerField(default=3)
    sheaps=models.IntegerField(null=True,blank=True)
    goats=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.Farmer

class child(models.Model):
    Parent=models.ForeignKey(family,on_delete=models.CASCADE)
    child_name=models.CharField(max_length=100 , default="XYZ")
    
    def __str__(self):
        return self.child_name+"\tof\tfather\t"+self.Parent.Farmer
    
class cow(models.Model):
    farmer=models.ForeignKey(family,on_delete=models.CASCADE)
    cow_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.cow_name+"\tof\tfarmer\t"+self.farmer.Farmer

class sheap(models.Model):
    farmer=models.ForeignKey(family,on_delete=models.CASCADE)
    sheap_name=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.sheap_name+"\tof\tfarmer\t"+self.farmer.Farmer

class goat(models.Model):
    farmer=models.ForeignKey(family,on_delete=models.CASCADE)
    goat_name=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.goat_name+"\tof\tfarmer\t"+self.farmer.Farmer

    