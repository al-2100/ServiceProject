FROM python:3.10-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias y archivos de la aplicación
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
