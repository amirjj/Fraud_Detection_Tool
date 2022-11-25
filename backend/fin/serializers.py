from rest_framework import serializers
from .models import PO

class POSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PO
        fields = ["Order_No", "Order_Code", "Order_Code_Description", "Status", "Supplier", "Supplier_Name", "Site", "Total_Net_Amt_Base", "Total_Net_Amt_Curr", "Tot_Tax_Amount_Curr", "Total_Gross_Amt_Curr", "Total_Gross_incl_Chrg_Curr", "Invoiced_Net_Amt_Invoice_Curr", "Invoicing_Supplier", "Invoicing_Supplier_Name", "Supplier_Contact", "Contact_Name", "Currency", "Language", "Created", "Wanted_Receipt_Date", "Label_Note", "Notes", "Forwarder_ID", "Supp_Order_No", "Ship_Via_Code", "Del_Terms", "Del_Terms_Location", "Payment_Terms", "Buyer", "Coordinator", "Revision_No", "Printed", "Schedule_Order", "Pay_Tax", "Document_Address", "Cancellation_Reason", "Cancellation_Reason_Description", "Centralized", "Internal_Destination_ID", "Internal_Destination_Description", "Delivery_Address", "Single_Occurrence", "Consolidated"]

