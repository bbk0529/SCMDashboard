from django.db import models


# Create your models here.




class Assay(models.Model):
    SA_No = models.IntegerField(primary_key=True)
    Date=models.CharField(max_length=30, blank=True,null=True)
    Number_of_suppliers=models.CharField(max_length=30,blank=True,null=True)
    Type	=models.CharField(max_length=50, blank=True,null=True)
    Details_1	=models.CharField(max_length=50, blank=True,null=True)
    Details_2	=models.CharField(max_length=50, blank=True,null=True)
    Description	=models.CharField(max_length=50, blank=True,null=True)
    Category	=models.CharField(max_length=50, blank=True,null=True)
    Updated_date=models.CharField(max_length=50, blank=True,null=True)


    Supplier1 =models.CharField(max_length=50, blank=True,null=True)
    Supplier1_Fabricating_Goods =models.CharField(max_length=50, blank=True,null=True)
    Supplier1_Modification_of_free_offerd_item =models.CharField(max_length=50, blank=True,null=True)
    Supplier1_Qty=models.CharField(max_length=50, blank=True,null=True)
    Supplier1_Final_Unit_Price	=models.CharField(max_length=50, blank=True,null=True)

    Supplier2 =models.CharField(max_length=50, blank=True,null=True)
    Supplier2_Fabricating_Goods =models.CharField(max_length=50, blank=True,null=True)
    Supplier2_Modification_of_free_offerd_item =models.CharField(max_length=50, blank=True,null=True)
    Supplier2_Qty=models.CharField(max_length=50, blank=True,null=True)
    Supplier2_Final_Unit_Price	=models.CharField(max_length=50, blank=True,null=True)

    Supplier3 =models.CharField(max_length=50, blank=True,null=True)
    Supplier3_Fabricating_Goods =models.CharField(max_length=50, blank=True,null=True)
    Supplier3_Modification_of_free_offerd_item =models.CharField(max_length=50, blank=True,null=True)
    Supplier3_Qty=models.CharField(max_length=50, blank=True,null=True)
    Supplier3_Final_Unit_Price =models.CharField(max_length=50, blank=True,null=True)

    Supplier4 =models.CharField(max_length=50, blank=True,null=True)
    Supplier4_Fabricating_Goods =models.CharField(max_length=50, blank=True,null=True)
    Supplier4_Modification_of_free_offerd_item =models.CharField(max_length=50, blank=True,null=True)
    Supplier4_Qty=models.CharField(max_length=50, blank=True,null=True)
    Supplier4_Final_Unit_Price	=models.CharField(max_length=50, blank=True,null=True)

    Supplier5 =models.CharField(max_length=50, blank=True,null=True)
    Supplier5_Fabricating_Goods =models.CharField(max_length=50, blank=True,null=True)
    Supplier5_Modification_of_free_offerd_item =models.CharField(max_length=50, blank=True,null=True)
    Supplier5_Qty=models.CharField(max_length=50, blank=True,null=True)
    Supplier5_Final_Unit_Price	=models.CharField(max_length=50, blank=True,null=True)


    Supplier6 =models.CharField(max_length=50, blank=True,null=True)
    Supplier6_Fabricating_Goods =models.CharField(max_length=50, blank=True,null=True)
    Supplier6_Modification_of_free_offerd_item =models.CharField(max_length=50, blank=True,null=True)
    Supplier6_Qty=models.CharField(max_length=50, blank=True,null=True)
    Supplier6_Final_Unit_Price	=models.CharField(max_length=50, blank=True,null=True)

class ChangeLog(models.Model):
    SA_No=models.IntegerField(blank=True,null=True)
    DateTime=models.DateTimeField(blank=True,null=True)
    User=models.CharField(blank=True,null=True,max_length=30)
    Field=models.CharField(blank=True,null=True,max_length=30)
    Before=models.CharField(max_length=50, blank=True,null=True)
    After=models.CharField(max_length=50, blank=True,null=True)
