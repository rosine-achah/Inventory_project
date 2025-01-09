from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    # Represents a category for inventory items.
    # Each category has a unique name and an optional description.
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            self.name
        )  # Returns the name of the category as its string representation.


class InventoryItem(models.Model):
    # Represents an inventory item in the store.
    # Each item belongs to a category and is associated with a user.
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="inventory_items"
    )

    def __str__(
        self,
    ):  #  Returns the name of the inventory item as its string representation
        return self.name


class InventoryChangeLog(models.Model):
    # Represents a log entry for changes made to an inventory item.
    # Tracks restocks and sales with details on the quantity changed and who made the change.
    inventory_item = models.ForeignKey(
        InventoryItem, on_delete=models.CASCADE, related_name="change_logs"
    )
    change_type = models.CharField(
        max_length=50, choices=[("restock", "Restock"), ("sale", "Sale")]
    )
    quantity_changed = models.IntegerField()
    change_date = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="change_logs"
    )

    def __str__(self):
        return f"{self.change_type} - {self.inventory_item.name}"

    def clean(self):
        # Validates that the quantity changed is non-negative.
        # Raises a ValidationError if the condition is not met.
        if self.quantity_changed < 0:
            raise ValidationError("Quantity changed must be non-negative.")
