from django.db import models
from django.contrib.auth.models import User



class RegisterUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.CharField(max_length=250,null=True,blank=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    about = models.TextField(blank=True,null=True)
    gender = models.CharField(max_length=250,default="Male")
    occupation = models.CharField(max_length=250,null=True,blank=True)
    added_on =models.DateTimeField(auto_now_add=True,null=True)
    update_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.user.username


