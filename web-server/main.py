from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return ["manzana","pera","Aguacate"]

@app.get("/contact")
def get_contact():
    return {"name" : "plazit"}

@app.get("/web", response_class=HTMLResponse)
def get_web():
    return """
        <h1>Hola soy una pagina web</h1>    
    """

