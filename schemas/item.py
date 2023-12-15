from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: str = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    # created_at: str
    # updated_at: str

class ItemUpdate(BaseModel):
    name: str
    description: str
