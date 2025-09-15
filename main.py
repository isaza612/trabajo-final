import uvicorn
import psycopg2
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, APIRouter

app = FastAPI()

# Configuración de CORS para permitir todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)


# Conexión simple a PostgreSQL
# def get_connection():
#     return psycopg2.connect(
#         dbname="pedido_db",
#         user="pedido",
#         password="pedido123",
#         host="localhost",
#         port="5432",
#     )
def get_connection():
    DB_HOST = os.getenv("DB_HOST", "host.docker.internal")
    DB_NAME = os.getenv("DB_NAME", "pedido_db")
    DB_USER = os.getenv("DB_USER", "pedido")
    DB_PASS = os.getenv("DB_PASS", "pedido123")
    DB_PORT = os.getenv("DB_PORT", "5432")
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
    )


@app.get("/api/statusserver", tags=["meta"])
def test():
    return {"status": "ok", "version": "2.0.0"}


# Insertar un registro (solo ID autoincremental)
@app.post("/api/orders")
def insert_order():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO orders DEFAULT VALUES RETURNING id;")
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": new_id}


# Listar registros
@app.get("/api/orders")
def list_orders():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM orders; ")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0]} for r in rows]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8083, access_log=False, log_config=None)
