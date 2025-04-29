from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from .import routes
from .database import Base, engine

Base.metadata.create_all(bind=engine)



app = FastAPI()

app.include_router(routes.router)

@app.get("/", response_class=HTMLResponse)
def root():
    return "<h2>Bienvenido a la API de Inventario</h2><p>Visita <a href='/docs'>/docs</a> para ver la documentación.</p>"
