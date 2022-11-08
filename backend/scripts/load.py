from fin.models import PO
i = 0
with open("tmpfiles/POs-8Oct22.csv", "r") as f:
    print(f)
    for line in f:
        print(line)
        break
        # lc = line.strip().split(",")
        # Fraud(msisdn=lc[0], fraud_description=lc[1], still_ongoing=True).save()