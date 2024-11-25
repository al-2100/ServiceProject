from fastapi import APIRouter, HTTPException
from src.services.user_service import UserService
from src.repositories.user_repository import UserRepository

router = APIRouter()

# Crear instancia del servicio
user_service = UserService(UserRepository())

# Definir las rutas

# Obtener todos los usuarios
@router.get("/users")
def get_users():
    return user_service.get_all()

# Obtener un usuario por su ID
@router.post("/users")
def create_user(name: str, email: str, password: str):
    try:
        return user_service.create(name, email, password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Crear un nuevo usuario
@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    user = user_service.delete(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

# Actualizar un usuario
@router.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str, password: str):
    user = user_service.update(user_id, name, email, password)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
