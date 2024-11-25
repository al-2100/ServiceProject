from typing import List, Optional
from src.services.base import BaseService
from src.repositories.user_repository import UserRepository
from src.models import User

class UserService(BaseService):
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_all(self) -> List[User]:
        return self.user_repo.get_all()

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.user_repo.get_by_id(user_id)

    def create(self, name: str, email: str, password: str) -> User:
        user = User(name=name, email=email, password=password)
        return self.user_repo.create(user)

    def delete(self, user_id: int) -> Optional[User]:
        return self.user_repo.delete(user_id)
