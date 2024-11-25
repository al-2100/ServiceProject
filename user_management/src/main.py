from fastapi import FastAPI
from src.controllers.user_controller import router

# Crear instancia de la aplicación FastAPI
app = FastAPI(
    title="User Management API",
    description="API para gestionar usuarios con operaciones CRUD.",
)

# Registrar las rutas
app.include_router(router, prefix="/api", tags=["Users"])

# Iniciar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
