from rest_framework import viewsets, mixins
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer

class CategoryViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """Read-only endpoints for categories: list and detail."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """Read-only endpoints for products: list and detail.

    Supports filtering with query parameters:
      ?category=<id>   only products in that category
      ?search=<text>   products whose name contains the text
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        category = self.request.query_params.get("category")
        search = self.request.query_params.get("search")
        if category:
            queryset = queryset.filter(category_id=category)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset
    
class OrderViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """Endpoints for orders: create, list, and detail."""   
    queryset = Order.objects.all()                         
    serializer_class = OrderSerializer                 