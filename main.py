import os, requests
from fastapi import FastAPI

app = FastAPI()
NOTIF_SERVICE_URL = os.getenv("NOTIF_SERVICE_URL") # URL interna de Railway

@app.post("/enviar")
def enviar_dato(nombre: str):
    # Envía el dato al Microservicio B
    response = requests.post(f"{NOTIF_SERVICE_URL}/procesar", json={"user": nombre})
    return {"status": "Enviado a Micro B", "respuesta_B": response.json()}
