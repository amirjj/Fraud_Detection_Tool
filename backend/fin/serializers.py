from rest_framework import serializers
from .models import PO

#TODO: checkout result for APIs are working well
class POSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PO
        fields = ["Order_No", "Order_Code", "Order_Code_Description", "Status", "Supplier", "Supplier_Name", "Site", "Total_Net_Amt_Base", "Total_Net_Amt_Curr", "Tot_Tax_Amount_Curr", "Total_Gross_Amt_Curr", "Total_Gross_incl_Chrg_Curr", "Invoiced_Net_Amt_Invoice_Curr", "Invoicing_Supplier", "Invoicing_Supplier_Name", "Supplier_Contact", "Contact_Name", "Currency", "Language", "Created", "Wanted_Receipt_Date", "Label_Note", "Notes", "Forwarder_ID", "Supp_Order_No", "Ship_Via_Code", "Del_Terms", "Del_Terms_Location", "Payment_Terms", "Buyer", "Coordinator", "Revision_No", "Printed", "Schedule_Order", "Pay_Tax", "Document_Address", "Cancellation_Reason", "Cancellation_Reason_Description", "Centralized", "Internal_Destination_ID", "Internal_Destination_Description", "Delivery_Address", "Single_Occurrence", "Consolidated"]


class DupAmountSameSupSerializer(serializers.Serializer):
    Supplier = serializers.CharField(max_length = 100)
    Total_Net_Amt_Base = serializers.FloatField()
    Status = serializers.CharField(max_length = 20)
    count = serializers.IntegerField()
    
class SplitPOSerializer(serializers.Serializer):
    Supplier = serializers.CharField(max_length = 100)
    Total_Net_Amt_Base = serializers.FloatField()
    Created = serializers.DateField()
    count = serializers.IntegerField()

class SumOfPOPerSupSerializer(serializers.Serializer):
    Supplier_Name = serializers.CharField(max_length = 500)
    total_count = serializers.IntegerField()


class POCountPerSupSerializer(serializers.Serializer):
    Supplier_Name = serializers.CharField(max_length = 500)
    total_count = serializers.IntegerField()

