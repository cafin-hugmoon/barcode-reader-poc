from django.db import models
from datetime import date, timedelta

def two_weeks_from_now():
    """Return a date two weeks from today."""
    return date.today() + timedelta(weeks=2)

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=50)  # e.g., "160g"
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField(default=two_weeks_from_now)

    def __str__(self):
        return f"{self.name} ({self.amount}, Quantity: {self.quantity})"
