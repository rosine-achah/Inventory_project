from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'), # Endpoint for user registration. Maps to a view for creating new users.

    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),     # Endpoint for retrieving, updating, or deleting details of a specific user by their primary key (id).

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint for obtaining JWT access and refresh tokens using username and password.
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint for refreshing the JWT access token using the refresh token.
    

    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),# Endpoint for listing all categories or creating a new category.
    path('inventory-items/', views.InventoryItemListCreateView.as_view(), name='inventory-item-list-create'),  # Endpoint for listing all inventory items or creating a new inventory item.
    path('inventory-items/<int:pk>/', views.InventoryItemDetailView.as_view(), name='inventory-item-detail'),  # Endpoint for retrieving, updating, or deleting a specific inventory item by its primary key (id).

    path('inventory-changes/', views.InventoryChangeLogListView.as_view(), name='inventory-change-log-list'), 
    #Endpoint for viewing all change logs of inventory items
]
