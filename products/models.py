from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=50)
    unit_price = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = (
        ('none', 'None'),
        ('color', 'Color'),
        ('size', 'Size'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

    def total_price(self):
        if self.discount:
            return int(((100 - self.discount)/ 100) * self.unit_price)
        else:
            return self.unit_price
