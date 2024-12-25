from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView
from .models import InventoryChange
from .serializers import InventoryChangeSerializer


class InventoryItemList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category", "price", "quantity"]

    def get_queryset(self):
        return InventoryItem.objects.filter(user=self.request.user)


class InventoryItemList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = InventoryItem.objects.filter(user=request.user)
        serializer = InventoryItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryChangeList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InventoryChangeSerializer

    def get_queryset(self):
        return InventoryChange.objects.filter(inventory_item_user=self.request.user)
