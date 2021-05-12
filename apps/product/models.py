from django.db import models
from datetime import datetime
from django.utils.translation import gettext as _


# from django.contrib.auth.models import User
 
class Team(models.Model):
    designation= models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.designation


class Item(models.Model):
    name = models.CharField(max_length=50)
    model_no = models.CharField(max_length=50)
    status   = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_now=True)
    catagory = models.ForeignKey("Catagory", on_delete=models.CASCADE)
    # employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Catagory(models.Model):
    name= models.CharField(max_length=50)
    add_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
  
    name = models.CharField(max_length=50)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField()

    class Meta:
        ordering = ['-id']
        


    
    def __str__(self):
        return self.email



class AssignItem(models.Model):
    employee= models.ForeignKey("Employee", on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    submit_date=models.DateTimeField(auto_now=True)
    expire_date=models.DateTimeField(null=True,blank=True)
    # status=models.CharField(max_length=50,null=False)
    def __str__(self):
        return self.employee
            