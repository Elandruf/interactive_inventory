from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
from .database import SessionLocal

router = APIRouter()

# Dependency para obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todos los ítems
@router.get("/items", response_model=List[schemas.ItemOut])
def get_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()

# Obtener un ítem por ID
@router.get("/items/{item_id}", response_model=schemas.ItemOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Crear un nuevo ítem
@router.post("/items", response_model=schemas.ItemOut)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Item).filter(models.Item.name == item.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Item with this name already exists")
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Actualizar ítem existente
@router.put("/items/{item_id}", response_model=schemas.ItemOut)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db_item.name = item.name
    db_item.quantity = item.quantity
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

# Eliminar ítem
@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}
