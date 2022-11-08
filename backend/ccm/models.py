from django.db import models

# Create your models here.

class DARoutines(models.Model):
    sequence_number = models.IntegerField()
    area = models.CharField(max_length = 50)
    report = models.TextField()
    objective = models.TextField()
    
    def __str__(self):
        print(self.report)

