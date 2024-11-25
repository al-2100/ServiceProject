import pytest
from httpx import AsyncClient
from product_catalog.src.main import app
from product_catalog.src.database import database
from product_catalog.src.models import Product
from unittest.mock import AsyncMock, patch

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    database.connect()
    database.create_tables([Product])
    yield
    database.drop_tables([Product])
    database.close()

@pytest.fixture
def client():
    return AsyncClient(app=app, base_url="http://test")

@pytest.mark.asyncio
async def test_create_product_with_valid_user(client):
    with patch("product_catalog.src.services.product_service.UserService") as user_service_mock:
        user_service_mock.return_value.get_by_id = AsyncMock(return_value={"id": 1, "name": "Jorge Barriga"})
        response = await client.post(
            "/api/products",
            json={"name": "Laptop", "description": "Gaming Laptop", "owner_id": 1}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Laptop"
        assert data["owner"]["id"] == 1

@pytest.mark.asyncio
async def test_create_product_with_invalid_user(client):
    with patch("product_catalog.src.services.product_service.UserService") as user_service_mock:
        user_service_mock.return_value.get_by_id = AsyncMock(return_value=None)
        response = await client.post(
            "/api/products",
            json={"name": "Laptop", "description": "Gaming Laptop", "owner_id": 99}
        )
        assert response.status_code == 400
        assert response.json()["detail"] == "Usuario con ID 99 no existe."
