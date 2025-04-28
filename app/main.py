from fastapi import FastAPI
from .models import Item 
from .routes import router  

app = FastAPI()


app.include_router(router)