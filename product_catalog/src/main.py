from fastapi import FastAPI
from src.controllers.product_controller import router

# Crear app
app = FastAPI(
    title="Product Catalog API",
    description="API para gestionar productos con operaciones CRUD.",
)

# Registrar las rutas
app.include_router(router, prefix="/api", tags=["Products"])

# Iniciar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8001, reload=True)
