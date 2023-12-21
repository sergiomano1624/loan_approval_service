from sqlalchemy.orm import Session
from models.LoanStatus import LoanStatus
from schemas.LoanStatus import LoanStatusCreate, LoanStatusUpdate, LoanStatusChangeStatus
from datetime import datetime
from uuid import UUID


def createLoanStatus(db: Session, data: LoanStatusCreate):
    db_item = LoanStatus(**data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def getLoanStatusByID(db: Session, id: UUID):
    return db.query(LoanStatus).filter(LoanStatus.id == id, LoanStatus.deleted_at.is_(None)).first()
    # return db.query(LoanStatus).filter(LoanStatus.id == id).first()

def getLoanStatus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LoanStatus).filter(LoanStatus.deleted_at.is_(None)).offset(skip).limit(limit).all()
    # return db.query(LoanStatus).offset(skip).limit(limit).all()


def updateLoanStatus(db: Session, item_id: UUID, item: LoanStatusUpdate):
    db_item = db.query(LoanStatus).filter(LoanStatus.id == item_id).first()
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def changeLoanStatus(db: Session, item_id: UUID, req: LoanStatusChangeStatus):
    getData = db.query(LoanStatus).filter(LoanStatus.id == item_id).first()
    if getData:
        getData.status = req.status
        db.commit()

