FROM python:3.12-slim

# Evita prompts interactivos y acelera instalación
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código
COPY . .

# Puerto de tu app (usa 9090 como en tu main.py)
EXPOSE 8083

# Variables por defecto (se pueden sobrescribir al correr)
ENV DB_HOST=host.docker.internal \
    DB_NAME=pedido_db \
    DB_USER=pedido \
    DB_PASS=pedido123 \
    DB_PORT=5432

# Comando de arranque
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8083"]
