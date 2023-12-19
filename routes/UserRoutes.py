from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config import db as database
from services import UserService as services
from schemas.Users import Users, UserCreate, UserUpdate, UserChangeStatus
# from utils.jwt import create_access_token, decode_token
from datetime import timedelta
from uuid import UUID

Userrouter = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

ACCESS_TOKEN_EXPIRE_MINUTES = 30

@Userrouter.post("/", response_model=Users)
def create_user(item: UserCreate, db: Session = Depends(get_db)):
    return services.createUser(db, item)
    # return {
    #     "status": 200,
    #     "message": "Created successfully"
    # }

@Userrouter.get("/{id}", response_model=Users)
def read_user(id: UUID, db: Session = Depends(get_db)):
    db_item = services.getUserByID(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_item

@Userrouter.get("/", response_model=list[Users])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.getUsers(db, skip, limit)

@Userrouter.put("/{id}", response_model=Users)
def update_user(id: UUID, item: UserUpdate, db: Session = Depends(get_db)):
    db_item = services.getUserByID(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return services.updateUser(db, id, item)

@Userrouter.put("/{id}/status", response_model=Users)
def change_status(id: UUID, req: UserChangeStatus, db: Session = Depends(get_db)):
    db_item = services.getUserByID(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    services.changeUserStatus(db, id, req)
    return db_item

@Userrouter.put("/{id}/delete", response_model=Users)
def delete_user(id: UUID, deleted_by: str, db: Session = Depends(get_db)):
    db_item = services.getUserByID(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    services.deleteUser(db, id, deleted_by)
    return db_item

# @Userrouter.post("/login", response_model=dict)
# def login_user(user: UserAuthCreate, db: Session = Depends(get_db)):
#     db_user = services.getUserEmail(db, email=user.email)
#     if db_user and services.verify_password(user.password, db_user.password):
#         access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#         access_token = create_access_token(
#             data={"sub": db_user.email}, expires_delta=access_token_expires
#         )
#         return {"access_token": access_token, "token_type": "bearer", "email": db_user.email, "role_type": db_user.user_type, "id": db_user.id}
#         return db_user
#     raise HTTPException(status_code=401, detail="Invalid credentials")