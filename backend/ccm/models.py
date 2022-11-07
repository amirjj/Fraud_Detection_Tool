from django.db import models

# Create your models here.

class DARoutines(models.Model):
    sequence_number = models.IntegerField()
    area = models.CharField()
    report = models.CharField()
    objective = models.CharField()
    
    def __str__(self):
        print(self.report)

