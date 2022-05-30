from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from products.models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated


class ProductsListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
