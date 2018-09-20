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

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

"""
from loteam.models import Publisher, Book
Publisher.objects.create(name='James Adams',address='baker street 221b')
Book.objects.create(title='Sherlok Homes', publisher=Publisher.objects.get(pk=1))


from loteam.models import YCP4, Ymon


"""


class Clearing(models.Model):
    Material=models.IntegerField()


class YCP4(models.Model):
    Material = models.IntegerField(primary_key=True)
    Description=models.CharField(max_length=30, blank=True,null=True)
    Con3M=models.IntegerField(blank=True,null=True)
    Con12M=models.IntegerField(blank=True,null=True)
    Stock=models.IntegerField(blank=True,null=True)
    Incoming=models.IntegerField(blank=True,null=True)
    Order=models.IntegerField(blank=True,null=True)
    Status=models.IntegerField(blank=True,null=True)
    Mrp=models.CharField(max_length=2, blank=True, null=True)
    MaterialType=models.CharField(max_length=4, blank=True, null=True)

class Ymon(models.Model):
    ycp4=models.ForeignKey(YCP4,on_delete=models.CASCADE)
    #Category=models.CharField(max_length=20, blank=True, null=True)
    U=models.CharField(max_length=1, blank=True,null=True)
    Sold_To_Party=models.IntegerField(blank=True,null=True)
    Name_1=models.CharField(max_length=30, blank=True,null=True)
    Sales_Document=models.CharField(max_length=10, blank=True,null=True)
    Item=models.CharField(max_length=2, blank=True,null=True)
    Purchase_order_no=models.CharField(max_length=10, blank=True,null=True)
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
    Remark=models.CharField(max_length=10, blank=True, null=True)
    Topticket=models.IntegerField(blank=True,null=True)
    Shippingcondition=models.CharField(max_length=2, blank=True,null=True)




class Material(models.Model):
    Pn=models.IntegerField()
    Type=models.CharField(max_length=10)
    Category=models.CharField(max_length=20)
    Description=models.CharField(max_length=40)


class Consumption(models.Model):
    Pn=models.IntegerField()
    Date=models.DateField()
    Qty=models.IntegerField()


class ProductFamily(models.Model):
    Product=models.CharField(max_length=20)
    SGFCode=models.CharField(max_length=20)
    Focus=models.CharField(max_length=20)
    Pn=models.CharField(max_length=20)


class Masterdata(models.Model):
    Material=models.IntegerField()
    Description=models.CharField(max_length=50, blank=True, null=True)
    TypeDescription=models.CharField(max_length=50, blank=True, null=True)
    Segmentation=models.CharField(max_length=5, blank=True, null=True)
    Hierarchy=models.CharField(max_length=20, blank=True, null=True)
    Type=models.CharField(max_length=5, blank=True, null=True)
    SupplyPlant=models.IntegerField(blank=True, null=True)
    SS0015=models.IntegerField(blank=True, null=True)
    Outlier0015=models.IntegerField( blank=True, null=True)
    SS0360=models.IntegerField( blank=True, null=True)
    Outier0360=models.IntegerField( blank=True, null=True)
    Con0015=models.IntegerField( blank=True, null=True)
    Con0360=models.IntegerField( blank=True, null=True)
    Vendor=models.IntegerField( blank=True, null=True)
