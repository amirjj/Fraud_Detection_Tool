from django.db import models
from fin.models import PO


class DARoutines(models.Model):
    sequence_number = models.IntegerField()
    area = models.CharField(max_length = 50)
    report = models.TextField()
    objective = models.TextField()
    
    def __str__(self):
        print(self.report)


class Fraud_schemes(models.Model):
    fraud_scheme_id = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    description = models.TextField()
    # fraud_category = models.ForeignKey(Fraud_Category)
    
