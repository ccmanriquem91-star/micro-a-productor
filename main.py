import os, requests
from fastapi import FastAPI

app = FastAPI()

# Railway lee esta variable de tu panel de Variables
NOTIF_SERVICE_URL = os.getenv("NOTIF_SERVICE_URL")

@app.get("/")
def home():
    return {"status": "Micro A Online", "manual": "Usa /enviar?nombre=TuNombre"}

@app.get("/enviar")
def enviar_dato(nombre: str = "Invitado"):
    try:
        # El Micro B sigue esperando un POST, así que el Micro A hace la conversión
        target_url = f"{NOTIF_SERVICE_URL}/procesar"
        payload = {"user": nombre}
        
        # Petición interna de Micro A (GET) a Micro B (POST)
        response = requests.post(target_url, json=payload, timeout=5)
        
        return {
            "mensaje": f"¡Éxito! Micro A recibió a '{nombre}'",
            "respuesta_del_micro_b": response.json(),
            "meta_data": "Comunicación HTTP Exitosa"
        }
    except Exception as e:
        return {"error": str(e), "ayuda": "Verifica que NOTIF_SERVICE_URL en Railway sea correcta"}
