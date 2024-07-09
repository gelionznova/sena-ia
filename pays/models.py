from django.db import models

class Pay(models.Model):
    pay_money = models.CharField(max_length=20, blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pay_money)
