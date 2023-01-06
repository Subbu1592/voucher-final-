from django.db import models


# Create your models here.

choices = (
    ('card', 'card'),
    ('cash', 'cash'),
    ('digital pay', 'digital pay'),


)
class Voucher(models.Model):
    date = models.DateField(auto_now=False)
    voucher_no = models.IntegerField()
    paid_to = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    amount = models.IntegerField()
    paid_by = models.CharField(max_length=100, null=True)
    approved_by = models.CharField(max_length=100)
    
    payment_mode = models.CharField(choices=choices, max_length=100,  blank=True ,null=True)
    card_details = models.CharField(max_length=100, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    on_account_of = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self) -> str:
        return self.paid_to 