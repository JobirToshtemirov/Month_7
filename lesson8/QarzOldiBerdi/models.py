from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)


class Debt(models.Model):
    borrower = models.ForeignKey(CustomUser, related_name='borrowed_debts', on_delete=models.CASCADE)
    lender = models.ForeignKey(CustomUser, related_name='lent_debts', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.amount} from {self.lender} to {self.borrower}"
