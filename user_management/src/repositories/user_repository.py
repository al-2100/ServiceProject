from typing import List, Optional
from src.repositories.base import BaseRepository
from src.models import User

class UserRepository(BaseRepository):
    def get_all(self) -> List[User]:
        return list(User.select())

    def get_by_id(self, user_id: int) -> Optional[User]:
        try:
            return User.get(User.id == user_id)
        except User.DoesNotExist:
            return None

    def create(self, user: User) -> User:
        return User.create(name=user.name, email=user.email, password=user.password)

    def delete(self, user_id: int) -> Optional[User]:
        user = self.get_by_id(user_id)
        if user:
            user.delete_instance()
        return user
