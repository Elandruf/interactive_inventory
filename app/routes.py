
from fastapi import APIRouter
from .models import Item

router = APIRouter()

# Lista que actuará como "base de datos" en memoria
inventory = []

@router.get("/items")
def get_items():
    return inventory

@router.post("/items")
def add_item(item: Item):
    inventory.append(item)
    return item