from django.db import models


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

    def __str__(self):
        return self.Order_No

    #develpe an instance method for queries
