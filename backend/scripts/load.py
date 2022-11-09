from fin.models import PO
from datetime import datetime

i = 0
with open("tmpfiles/POs-8Oct22.csv", "r") as f:
    for line in f:
        if "Order" not in line:
            lc = line.strip().split(",")
            PO(
                Order_No = lc[0],
                Order_Code = lc[1],
                Order_Code_Description = lc[2],
                Status = lc[3],
                Supplier = lc[4],
                Supplier_Name = lc[5],
                Site = lc[6],
                Total_Net_Amt_Base = lc[7],
                Total_Net_Amt_Curr = lc[8],
                Tot_Tax_Amount_Curr = lc[9],
                Total_Gross_Amt_Curr = lc[10],
                Total_Gross_incl_Chrg_Curr = lc[11],
                Invoiced_Net_Amt_Invoice_Curr = lc[12],
                Invoicing_Supplier = lc[13],
                Invoicing_Supplier_Name = lc[14],
                Supplier_Contact = lc[15],
                Contact_Name = lc[16],
                Currency = lc[17],
                Language = lc[18],
                Created = datetime.strptime(lc[19], "%m/%d/%Y"),
                Wanted_Receipt_Date = datetime.strptime(lc[20], "%m/%d/%Y"),
                Label_Note = lc[21],
                Notes = lc[22],
                Forwarder_ID = lc[23],
                Supp_Order_No = lc[24],
                Ship_Via_Code = lc[25],
                Del_Terms = lc[26],
                Del_Terms_Location = lc[27],
                Payment_Terms = lc[28],
                Buyer = lc[29],
                Coordinator = lc[30],
                Revision_No = lc[31],
                Printed = lc[32],
                Schedule_Order = lc[33],
                Pay_Tax = lc[34],
                Document_Address = lc[35],
                Cancellation_Reason = lc[36],
                Cancellation_Reason_Description = lc[37],
                Centralized = lc[38],
                Internal_Destination_ID = lc[39],
                Internal_Destination_Description = lc[40],
                Delivery_Address = lc[41],
                Single_Occurrence = lc[42],
                Consolidated = lc[43]
            ).save()
            