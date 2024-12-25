from django.contrib.auth.models import User
from django.db import models


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="inventory_items"
    )

    def __str__(self):
        return self.name


class InventoryChange(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete= models.CASCADE, related_name='changes')
    change_quantity = models.IntegerField()
    change_date = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Change: {self.change_quantity} for {self.inventory_item.name}"