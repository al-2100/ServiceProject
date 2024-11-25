from typing import List, Optional
from src.repositories.base import BaseRepository
from src.models import Product

class ProductRepository(BaseRepository):
    def get_all(self) -> List[Product]:
        return list(Product.select())

    def get_by_id(self, product_id: int) -> Optional[Product]:
        try:
            return Product.get(Product.id == product_id)
        except Product.DoesNotExist:
            return None

    def create(self, product: Product) -> Product:
        return Product.create(name=product.name, description=product.description, owner=product.owner)

    def delete(self, product_id: int) -> Optional[Product]:
        product = self.get_by_id(product_id)
        if product:
            product.delete_instance()
        return product
