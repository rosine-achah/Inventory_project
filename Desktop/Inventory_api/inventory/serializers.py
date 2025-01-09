from rest_framework import serializers
from .models import Category, InventoryItem, InventoryChangeLog
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Hash the password and create a user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'date_added']


class InventoryItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, source='category'
    )

    class Meta:
        model = InventoryItem
        fields = [
            'id', 'name', 'description', 'quantity', 'price', 
            'category', 'category_id', 'date_added', 'last_updated'
        ]

    
    def update(self, instance, validated_data):
        user = self.context['request'].user
        new_quantity = validated_data.get('quantity', instance.quantity)

        # Log change if quantity differs
        if instance.quantity != new_quantity:
            change_type = 'restock' if new_quantity > instance.quantity else 'sale'
            quantity_diff = abs(new_quantity - instance.quantity)
            InventoryChangeLog.objects.create(
                inventory_item=instance,
                change_type=change_type,
                quantity_changed=quantity_diff,
                changed_by=user
            )

        return super().update(instance, validated_data)


class InventoryChangeLogSerializer(serializers.ModelSerializer):
    changed_by = serializers.StringRelatedField()
    inventory_item = serializers.StringRelatedField()

    class Meta:
        model = InventoryChangeLog
        fields = ['id', 'inventory_item', 'change_type', 'quantity_changed', 'change_date', 'changed_by']