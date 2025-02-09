from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Calculation(models.Model):

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField("created")
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    operation = models.CharField(max_length=200)
    answer = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.operation}({self.x}, {self.y}) = {self.answer}"
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
 

