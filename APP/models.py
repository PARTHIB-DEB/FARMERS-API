from django.db import models

# Create your models here.

class child(models.Model):
    child_name=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.child_name
    
class cow(models.Model):
    cow_name=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.cow_name

class sheap(models.Model):
    sheap_name=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.sheap_name

class goat(models.Model):
    goat_name=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.goat_name

class family(models.Model):
    Farmer=models.CharField(max_length=100)
    Wife=models.CharField(max_length=100)
    children=models.IntegerField(null=True,blank=True)
    child_names=models.ForeignKey(child,null=True,blank=True,related_name="name_child",on_delete=models.CASCADE)
    cows=models.IntegerField(null=True,blank=True)
    cow_names=models.ForeignKey(cow,null=True,blank=True,related_name="name_cow",on_delete=models.CASCADE)
    sheaps=models.IntegerField(null=True,blank=True)
    sheap_names=models.ForeignKey(sheap,null=True,blank=True,related_name="name_sheap",on_delete=models.CASCADE)
    goats=models.IntegerField(null=True,blank=True)
    goat_names=models.ForeignKey(goat,null=True,blank=True,related_name="name_goat",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Farmer

    