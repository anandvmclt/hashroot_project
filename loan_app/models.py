#hashroot_project/loan_app/models.py
from django.db import models

class ReverseMortgage(models.Model):
    age = models.PositiveIntegerField()
    home_value = models.FloatField()
    margin = models.FloatField()
    principal_limit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reverse Mortgage for age {self.age} and home value {self.home_value}"