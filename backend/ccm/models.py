from django.db import models
from fin.models import PO


class DARoutines(models.Model):
    sequence_number = models.IntegerField()
    area = models.CharField(max_length = 50)
    report = models.TextField()
    objective = models.TextField()
    
    def __str__(self):
        print(self.report)


class Fraud_category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Fraud_schemes(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    fraud_category = models.ForeignKey(Fraud_category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

