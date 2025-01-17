from django.db import models

# Create your models here.

class Stock(models.Model):
    stock_name = models.CharField(max_length=50)
    stock_code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.stock_name} ({self.stock_code})"

    class Meta:
        ordering = ['stock_name']
