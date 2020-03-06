from django.db import models

class Merchant(models.Model):
    name = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    description = models.CharField(max_length=120,null=True,blank=True)
    city = models.CharField(max_length=120,null=True,blank=True)
    state = models.CharField(max_length=120,null=True,blank=True)
    country = models.CharField(max_length=120,null=True,blank=True)
    sublocality = models.CharField(max_length=120,null=True,blank=True) 
    zipcode = models.CharField(max_length=120,null=True,blank=True)
    phone = models.CharField(max_length=120,null=True,blank=True)
    email = models.CharField(max_length=120,null=True,blank=True)
    mvp = models.BooleanField(default=False)
    last_active = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name