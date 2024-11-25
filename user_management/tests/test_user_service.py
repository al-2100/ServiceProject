import pytest
from unittest.mock import MagicMock
from user_management.src.services.user_service import UserService
from user_management.src.models import User

@pytest.fixture
def user_repo_mock():
    return MagicMock()

@pytest.fixture
def user_service(user_repo_mock):
    return UserService(user_repo_mock)

def test_get_all_users(user_service, user_repo_mock):
    user_repo_mock.get_all.return_value = [
        User(id=1, name="Jorge Barriga", email="jorge.barriga@example.com", password="1234")
    ]
    users = user_service.get_all()
    assert len(users) == 1
    assert users[0].name == "Jorge Barriga"

def test_create_user(user_service, user_repo_mock):
    user_data = {"name": "Jorge Barriga", "email": "jorge.barriga@example.com", "password": "1234"}
    user_repo_mock.create.return_value = User(id=1, **user_data)
    user = user_service.create(**user_data)
    assert user.name == "Jorge Barriga"
    assert user.email == "jorge.barriga@example.com"
