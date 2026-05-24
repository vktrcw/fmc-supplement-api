import pytest
from decimal import Decimal
from rest_framework.test import APIClient
from catalog.models import Category, Product, Order, OrderItem


# ---------------------------------------------------------------------------
# Unit test: the Product model
# ---------------------------------------------------------------------------
@pytest.mark.django_db
def test_product_is_created_correctly():
    """A Product can be created and its fields are stored correctly."""
    category = Category.objects.create(name="Protein")
    product = Product.objects.create(
        category=category,
        name="FMC Whey Protein",
        description="Chocolate flavour whey protein.",
        price=Decimal("39.99"),
        stock=100,
    )

    assert product.name == "FMC Whey Protein"
    assert product.price == Decimal("39.99")
    assert product.stock == 100
    assert product.is_active is True
    assert product.category.name == "Protein"


# ---------------------------------------------------------------------------
# Integration test: the product list endpoint
# ---------------------------------------------------------------------------
@pytest.mark.django_db
def test_product_list_endpoint_returns_products():
    """GET /api/products/ returns the products in the database."""
    category = Category.objects.create(name="Vitamins")
    Product.objects.create(
        category=category,
        name="FMC Vitamin C",
        price=Decimal("12.50"),
        stock=50,
    )

    client = APIClient()
    response = client.get("/api/products/")

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "FMC Vitamin C"


# ---------------------------------------------------------------------------
# Integration test: creating an order
# ---------------------------------------------------------------------------
@pytest.mark.django_db
def test_create_order_endpoint():
    """POST /api/orders/ creates an order and records the price paid."""
    category = Category.objects.create(name="Pre-Workout")
    product = Product.objects.create(
        category=category,
        name="FMC Pre-Workout",
        price=Decimal("29.99"),
        stock=20,
    )

    client = APIClient()
    payload = {
        "customer_name": "Test Customer",
        "customer_email": "test@example.com",
        "items": [
            {"product": product.id, "quantity": 2},
        ],
    }
    response = client.post("/api/orders/", payload, format="json")

    assert response.status_code == 201
    assert Order.objects.count() == 1

    order_item = OrderItem.objects.get()
    assert order_item.quantity == 2
    assert order_item.unit_price == Decimal("29.99")