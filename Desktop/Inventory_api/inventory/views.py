from rest_framework import generics, permissions, filters
from .models import Category, InventoryItem, InventoryChangeLog
from .serializers import (
    CategorySerializer,
    InventoryItemSerializer,
    InventoryChangeLogSerializer,
    UserSerializer,
)
from .permissions import IsOwner
from django.contrib.auth.models import User


class UserRegisterView(generics.CreateAPIView):
    # Provides an endpoint for user registration.
    # Uses the UserSerializer for validation and creation of new users.
    # Authentication is not required to access this endpoint.

    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]  # No authentication required to register


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    # Provides endpoints for retrieving, updating, or deleting user details.
    # Only authenticated users can access this endpoint.
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users


class CategoryListCreateView(generics.ListCreateAPIView):
    #  Provides endpoints to list all categories or create a new category.
    # Only authenticated users can access this endpoint.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class InventoryItemListCreateView(generics.ListCreateAPIView):
    # Provides endpoints to list all inventory items or create a new inventory item.
    # Items can be filtered and ordered by specified fields.
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ["category", "price", "quantity"]
    ordering_fields = ["name", "price", "quantity", "date_added"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InventoryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    # Provides endpoints for retrieving, updating, or deleting an inventory item.
    # Users can only access their own inventory items.
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Ensure users can only access their own inventory items
        return InventoryItem.objects.filter(user=self.request.user)


class InventoryChangeLogListView(generics.ListAPIView):
    #   Provides an endpoint to list change logs for inventory items.
    # Users can only view logs for items they own.
    queryset = InventoryChangeLog.objects.all()
    serializer_class = InventoryChangeLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Allow users to view change logs for their own items
        return InventoryChangeLog.objects.filter(inventory_item__user=self.request.user)
