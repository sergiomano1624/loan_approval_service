from sqlalchemy.orm import Session
from models.item import Item
from schemas.item import ItemCreate
from datetime import datetime

def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

def update_item(db: Session, item_id: int, item: ItemCreate):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int, deleted_by: str):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db_item.deleted_at = datetime.now()
        db_item.deleted_by = deleted_by
        db.commit()
