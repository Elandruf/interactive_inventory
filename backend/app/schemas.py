from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int
    is_active: bool = True

class ItemCreate(ItemBase):
    pass

class ItemOut(ItemBase):
    id: int

    model_config={
        "from_atributtes": True
    }