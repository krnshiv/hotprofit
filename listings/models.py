from django.db import models
from datetime import datetime
from merchants.models import Merchant
from taggit.managers import TaggableManager

category_choices={
    ('BR','Bread/Bakery'),
    ('DA', 'Dairy'),
    ('CG', 'CannedGoods'),
    ('DBG', 'Dry/BakingGoods'),
    ('FR','fruits'),
    ('VEG', 'veggies'),
    ('HE','herbs'),
    ('SP', 'spices'),
    ('UT', 'utensils'),
    ('BEV', 'bevrages'),
    ('M', 'meat'),
    ('CL', 'cleaners'),
    ('PG', 'PaperGoods'),
    ('OT', 'others'),
}
class Listing(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE,null=True, blank=True, default=None)
    name = models.CharField(max_length=120,null=True, blank=True, default=None) 
    category = models.CharField(max_length=120,choices=category_choices,blank=True,default=None)
    brand = models.CharField(max_length=120,null=True, blank=True, default=None)
    tags =  TaggableManager(blank=True)
    oldprice = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default=None)
    newprice = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default=None)
    description= models.CharField(max_length=120,null=True, blank=True, default=None)
    qty = models.IntegerField(null=True, blank=True, default=None)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True,default='../static/img/fruits.png')
    posted = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)
    validity = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name
    
    