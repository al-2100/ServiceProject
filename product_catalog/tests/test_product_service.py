import pytest
from unittest.mock import MagicMock, patch
from product_catalog.src.services.product_service import ProductService
from product_catalog.src.models import Product

@pytest.fixture
def product_repo_mock():
    return MagicMock()

@pytest.fixture
def user_service_mock():
    return MagicMock()

@pytest.fixture
def product_service(product_repo_mock, user_service_mock):
    with patch("product_catalog.src.services.product_service.UserService", return_value=user_service_mock):
        return ProductService(product_repo_mock)

def test_create_product_valid_user(product_service, product_repo_mock, user_service_mock):
    user_service_mock.get_by_id.return_value = MagicMock(id=1, name="Jorge Barriga")
    product_repo_mock.create.return_value = Product(id=1, name="Laptop", description="Gaming Laptop", owner=1)
    product = product_service.create("Laptop", "Gaming Laptop", 1)
    assert product.name == "Laptop"
    assert product.owner.id == 1

def test_create_product_invalid_user(product_service, user_service_mock):
    user_service_mock.get_by_id.return_value = None
    with pytest.raises(ValueError, match="Usuario con ID 1 no existe."):
        product_service.create("Laptop", "Gaming Laptop", 1)
