from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    

    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'), #Create and View the different categories present
    path('inventory-items/', views.InventoryItemListCreateView.as_view(), name='inventory-item-list-create'), #Create and View the list of items 
    path('inventory-items/<int:pk>/', views.InventoryItemDetailView.as_view(), name='inventory-item-detail'), #View the details of a particular item 
    path('inventory-changes/', views.InventoryChangeLogListView.as_view(), name='inventory-change-log-list'), 
    #
]
