from django.db import models
from django.db.models import Sum, Count, Q, Subquery

#Good idea to store important queries in Model. important queires which are called (more than others) from views
#So Custome managers are needed, as Manager is the interface through which database query operation are provided
#reasons to use custome manager: to add extra Manager methods, to modify the initial QuerySet the Manager returns.
#Adding extra Manager methods is the preferred way to add "table-level" functionality to your models.
#for "row-level" functionality ie., functions act on a single instance of a model object need to use Model methods
#not custome Manager methods

class POQuerySet(models.QuerySet):
    
    def get_all_pos(self):
        return self

    def duplicate_amount_same_supplier(self):
        dups = self.values("Supplier", "Total_Net_Amt_Base", "Status").\
            annotate(count=Count("Total_Net_Amt_Base")).filter(count__gt=1).order_by('-count')
        return dups
        # dup_list = [item for item in dups]
        # print(dup_list)
        # return self.extra(where=['(Supplier, Total_Net_Amt_Base, new_class) in %s' % dup_list])
    
    def closed_counts(self):
        return self.filter(Status="Closed").count()

    def top_po_recieved_count(self):
        return self

    def sum_of_po_amounts_per_supp(self):
        return self.values('Supplier_Name').annotate(
            total_count=Sum('Total_Net_Amt_Base', filter=Q(Status="Closed")),
        ).order_by('-total_count')

    def po_count_per_supp(self):
        return self.values('Supplier_Name').annotate(
            total_count=Count('Order_No', filter=Q(Status="Closed")),
        ).order_by('-total_count')
        

class POManager(models.Manager):
    pass

class PO(models.Model):
    Order_No = models.CharField(max_length = 20)
    Order_Code = models.CharField(max_length = 20)
    Order_Code_Description = models.CharField(max_length = 355)
    Status = models.CharField(max_length = 20)
    Supplier = models.CharField(max_length = 100)
    Supplier_Name = models.CharField(max_length = 355)
    Site = models.CharField(max_length = 50)
    Total_Net_Amt_Base = models.FloatField()
    Total_Net_Amt_Curr = models.FloatField()
    Tot_Tax_Amount_Curr = models.FloatField()
    Total_Gross_Amt_Curr = models.FloatField()
    Total_Gross_incl_Chrg_Curr = models.FloatField()
    Invoiced_Net_Amt_Invoice_Curr = models.FloatField()
    Invoicing_Supplier = models.CharField(max_length = 60)
    Invoicing_Supplier_Name = models.CharField(max_length = 100)
    Supplier_Contact = models.CharField(max_length = 60)
    Contact_Name = models.CharField(max_length = 50)
    Currency = models.CharField(max_length = 10)
    Language = models.CharField(max_length = 10)
    Created = models.DateField()
    Wanted_Receipt_Date = models.DateField()
    Label_Note = models.CharField(max_length = 50)
    Notes = models.CharField(max_length = 100)
    Forwarder_ID = models.CharField(max_length = 50)
    Supp_Order_No = models.CharField(max_length = 60)
    Ship_Via_Code = models.CharField(max_length = 50)
    Del_Terms = models.CharField(max_length = 60)
    Del_Terms_Location = models.CharField(max_length = 60)
    Payment_Terms = models.CharField(max_length = 100)
    Buyer = models.CharField(max_length = 60)
    Coordinator = models.CharField(max_length = 40)
    Revision_No = models.IntegerField()
    Printed = models.CharField(max_length = 20)
    Schedule_Order = models.CharField(max_length = 40)
    Pay_Tax = models.CharField(max_length = 40)
    Document_Address = models.CharField(max_length = 255)
    Cancellation_Reason = models.CharField(max_length = 255)
    Cancellation_Reason_Description = models.TextField(max_length = 355)
    Centralized = models.CharField(max_length = 50)
    Internal_Destination_ID = models.CharField(max_length = 50)
    Internal_Destination_Description = models.TextField(max_length = 355)
    Delivery_Address = models.CharField(max_length = 355)
    Single_Occurrence = models.CharField(max_length = 20)
    Consolidated = models.CharField(max_length = 100)

    objects = models.Manager()
    custom_manager = POManager.from_queryset(POQuerySet)()

    def __str__(self):
        return self.Order_No


    #develpe an instance method for queries
