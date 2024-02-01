from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.name}, email: {self.email}'
