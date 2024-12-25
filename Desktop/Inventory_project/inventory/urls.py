from django.urls import path
from .views import InventoryItemList
from .views import InventoryChangeList

urlpatterns = [
    path("items/", InventoryItemList.as_view(), name="inventory-items"),
    path("items/changes/", InventoryChangeList.as_view(), name="inventory-changes"),
]
