from fastapi import APIRouter, HTTPException
from src.services.product_service import ProductService
from src.repositories.product_repository import ProductRepository

router = APIRouter()

# Instancia del servicio
product_service = ProductService(ProductRepository())

# Definir las rutas
@router.get("/products")
def get_products():
    return product_service.get_all()

# Obtener un producto por su ID
@router.post("/products")
def create_product(name: str, description: str, owner_id: int):
    try:
        return product_service.create(name, description, owner_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Crear un nuevo producto
@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    product = product_service.delete(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado"}

# Actualizar un producto
@router.put("/products/{product_id}")
def update_product(product_id: int, name: str, description: str, owner_id: int):
    product = product_service.update(product_id, name, description, owner_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product
