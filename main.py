import os, requests
from fastapi import FastAPI

app = FastAPI()

# Railway leerá esta variable desde el panel de Variables
NOTIF_SERVICE_URL = os.getenv("NOTIF_SERVICE_URL")

@app.get("/")
def home():
    return {"status": "Micro A Online", "manual": "Usa /enviar?nombre=TuNombre"}

@app.get("/enviar")
def enviar_dato(nombre: str = "Invitado"):
    # Construimos la URL del Microservicio B
    # El Micro B siempre espera un POST según el código anterior
    try:
        target_url = f"{NOTIF_SERVICE_URL}/procesar"
        payload = {"user": nombre}
        
        # Micro A (GET) -> Micro B (POST)
        response = requests.post(target_url, json=payload, timeout=5)
        
        return {
            "msg": f"Hola {nombre}, Micro A recibió tu dato",
            "micro_b_response": response.json(),
            "target": target_url
        }
    except Exception as e:
        return {"error": str(e), "tip": "Revisa que NOTIF_SERVICE_URL sea correcta"}
