from typing import List, Optional
from src.services.base import BaseService
from src.repositories.product_repository import ProductRepository
from src.models import Product


class ProductService(BaseService):
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def get_all(self) -> List[Product]:
        return self.product_repo.get_all()

    def get_by_id(self, product_id: int) -> Optional[Product]:
        return self.product_repo.get_by_id(product_id)

    def create(self, name: str, description: str, owner_id: int) -> Product:
        # Validación de existencia del usuario propietario
        from src.user_management.services.user_service import UserService
        user_service = UserService()
        owner = user_service.get_by_id(owner_id)
        if not owner:
            raise ValueError(f"Usuario con ID {owner_id} no existe.")

        product = Product(name=name, description=description, owner=owner)
        return self.product_repo.create(product)

    def delete(self, product_id: int) -> Optional[Product]:
        return self.product_repo.delete(product_id)
