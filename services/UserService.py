from sqlalchemy.orm import Session
from models.Users import Users
from schemas.Users import UserCreate, UserUpdate, UserChangeStatus, UserUpdateLastLogin
from datetime import datetime
from uuid import UUID
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def createUser(db: Session, data: UserCreate):
    # hashed_password = pwd_context.hash("test")
    db_item = Users(**data.dict())
    db_item.password = "test"
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def getUserByID(db: Session, id: UUID):
    return db.query(Users).filter(Users.id == id, Users.deleted_at.is_(None)).first()
    # return db.query(Users).filter(Users.id == id).first()

def getUsers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).filter(Users.deleted_at.is_(None)).offset(skip).limit(limit).all()
    # return db.query(Users).offset(skip).limit(limit).all()

def getUserEmail(db: Session, email: str):
    # print(email)
    return db.query(Users).filter(Users.email == email).first()

def updateUser(db: Session, item_id: UUID, item: UserUpdate):
    db_item = db.query(Users).filter(Users.id == item_id).first()
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def updateUserLastLogin(db: Session, item_id: UUID, item: UserUpdateLastLogin):
    db_item = db.query(Users).filter(Users.id == item_id).first()
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def changeUserStatus(db: Session, item_id: UUID, req: UserChangeStatus):
    getData = db.query(Users).filter(Users.id == item_id).first()
    if getData:
        getData.status = req.status
        db.commit()

def deleteUser(db: Session, id: UUID, deleted_by: str):
    db_item = db.query(Users).filter(Users.id == id).first()
    print(db_item.deleted_by)
    if db_item:
        db_item.deleted_at = datetime.now()
        db_item.deleted_by = deleted_by
        db.commit()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)