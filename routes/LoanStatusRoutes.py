from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config import db as database
from services import LoanStatusService as services
from schemas.LoanStatus import LoanStatus, LoanStatusCreate, LoanStatusUpdate, LoanStatusChangeStatus
# from utils.jwt import create_access_token, decode_token
from datetime import timedelta
from uuid import UUID

LoanStatusRouter = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@LoanStatusRouter.post("/", response_model=LoanStatus)
def create_LoanStatus(item: LoanStatusCreate, db: Session = Depends(get_db)):
    return services.createLoanStatus(db, item)

@LoanStatusRouter.get("/", response_model=list[LoanStatus])
def read_LoanStatus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.getLoanStatus(db, skip, limit)

@LoanStatusRouter.put("/{id}", response_model=LoanStatus)
def update_LoanStatus(id: UUID, item: LoanStatusUpdate, db: Session = Depends(get_db)):
    db_item = services.getLoanStatusByID(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return services.updateLoanStatus(db, id, item)

@LoanStatusRouter.put("/{id}/status", response_model=LoanStatus)
def change_status(id: UUID, req: LoanStatusChangeStatus, db: Session = Depends(get_db)):
    db_item = services.getLoanStatusByID(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    services.changeLoanStatustatus(db, id, req)
    return db_item

