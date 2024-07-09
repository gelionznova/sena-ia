from django.db import models

class Codeqr(models.Model):
    number_ticket = models.CharField(max_length=4, default='')  # Establecer un valor predeterminado
    number_one = models.CharField(max_length=4)
    number_two = models.CharField(max_length=4)
    image_qr= models.ImageField(upload_to="qr", default='')
    
    def __str__(self):
        return self.number_ticket

