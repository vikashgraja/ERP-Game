from django.db import models

# Create your models here.
class score(models.Model):
    employee_id = models.CharField(max_length=10)
    employee_name = models.CharField(default=None,max_length=30)
    attempts = models.IntegerField()
    start_time = models.DateTimeField(default=None, null=True)
    H_1 = models.CharField(max_length=2,null=True)
    H1t = models.IntegerField(default=2)
    H_2 = models.CharField(max_length=2,null=True)
    H2t = models.IntegerField(default=2)
    H_3 = models.CharField(max_length=2,null=True)
    H3t = models.IntegerField(default=2)
    H_4 = models.CharField(max_length=2,null=True)
    H4t = models.IntegerField(default=2)
    end_time = models.DateTimeField(default=None, null=True)
    time_taken = models.DurationField(default=None, null=True)
    marks = models.IntegerField(default=None, null=True)

    def __str__(self):
        return self.employee_id