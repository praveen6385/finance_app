from django.db import models

# Create your models here.
class Borrower(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_tenure = models.IntegerField()  # In months
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # In percentage
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # Calculate monthly EMI
    def calculate_emi(self):
        monthly_interest_rate = (self.interest_rate / 100) / 12
        numerator = self.loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** self.loan_tenure
        denominator = (1 + monthly_interest_rate) ** self.loan_tenure - 1
        emi = numerator / denominator
        return round(emi, 2)