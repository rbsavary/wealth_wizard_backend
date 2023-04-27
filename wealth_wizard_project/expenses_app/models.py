from django.db import models
from django.utils import timezone


# Create your models here.
class Expense(models.Model):
    date = models.DateField(("Date"), default=timezone.now)
    transaction = models.CharField(max_length=32)
    amount = models.IntegerField()

    def clean(self):
        if self.amount < 0:
            raise ValidationError("Amount cannot be negative.")
