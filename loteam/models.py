from django.db import models
from django.utils import timezone

class Post(models.Model):
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self) :
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self) : 
        return self.title

class Ymon(models.Model):
    Category=models.CharField(max_length=20, blank=True, null=True)
    U=models.CharField(max_length=1, blank=True,null=True)
    Sold_To_Party=models.IntegerField(blank=True,null=True)
    Name_1=models.CharField(max_length=30, blank=True,null=True)
    Sales_Document=models.CharField(max_length=10, blank=True,null=True)
    Item=models.CharField(max_length=2, blank=True,null=True)
    Purchase_order_no=models.CharField(max_length=10, blank=True,null=True)
    Material=models.CharField(max_length=10, blank=True,null=True)
    MRP_Type=models.CharField(max_length=2, blank=True,null=True)
    Description=models.CharField(max_length=30, blank=True,null=True)
    Ident_code_1=models.CharField(max_length=30, blank=True,null=True)
    Ident_code_2=models.CharField(max_length=30, blank=True,null=True)
    Order_Quantity=models.IntegerField(blank=True,null=True)
    Open_quantity=models.IntegerField(blank=True,null=True)
    Pos_created_on=models.DateField(blank=True,null=True)
    Actconf_date=models.DateField(blank=True,null=True)
    Requested_deliv_date=models.DateField(blank=True,null=True)
    Delta=models.IntegerField(blank=True, null=True)
    LT=models.IntegerField(blank=True, null=True)

    

class Material(models.Model):
    Pn=models.IntegerField()
    Type=models.CharField(max_length=10)
    Category=models.CharField(max_length=20)
    Description=models.CharField(max_length=40)
    
        
class Consumption(models.Model):
    Pn=models.IntegerField()
    Date=models.DateField()
    Qty=models.IntegerField()    
    