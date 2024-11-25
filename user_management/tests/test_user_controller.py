import pytest
from httpx import AsyncClient
from user_management.src.main import app
from product_catalog.src.database import database
from user_management.src.models import User

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    database.connect()
    database.create_tables([User])
    yield
    database.drop_tables([User])
    database.close()

@pytest.fixture
def client():
    return AsyncClient(app=app, base_url="http://test")

@pytest.mark.asyncio
async def test_create_user(client):
    response = await client.post(
        "/api/users",
        json={"name": "Jorge Barriga", "email": "jorge.barriga@example.com", "password": "1234"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jorge Barriga"

@pytest.mark.asyncio
async def test_get_users(client):
    response = await client.get("/api/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
