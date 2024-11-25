# Usamos una imagen base oficial de Python
FROM python:3.10-slim

# Configuramos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos y lo instalamos
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente del proyecto al contenedor
COPY . .

# Exponemos el puerto en el que se ejecutará FastAPI
EXPOSE 8000

# Comando para iniciar la API
CMD ["python", "-m", "src.main"]
