from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config import db as database
from services import item_service as item_service
from schemas.item import Item, ItemCreate, ItemUpdate

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/items", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(db, item)
    # return {
    #     "status": 200,
    #     "message": "Created successfully"
    # }

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = item_service.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.get("/items", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return item_service.get_items(db, skip, limit)

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = item_service.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_service.update_item(db, item_id, item)

@router.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int, deleted_by: str, db: Session = Depends(get_db)):
    db_item = item_service.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item_service.delete_item(db, item_id, deleted_by)
    return db_item