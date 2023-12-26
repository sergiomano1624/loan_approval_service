from fastapi import APIRouter, Depends, HTTPException, File, Form, UploadFile
from sqlalchemy.orm import Session
from config import db as database
from services import LoanPaymentService as services
from schemas.Documents import Documents
from schemas.LoanPayments import LoanPayments, LoanPaymentCreate, LoanPaymentUpdate, LoanPaymentChangeStatus
# from utils.jwt import create_access_token, decode_token
from datetime import timedelta

LoanPaymentRouter = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@LoanPaymentRouter.get("/{loan_application_id}", response_model=list[LoanPayments])
def read_loan_payment(loan_application_id: int, db: Session = Depends(get_db)):
    db_item = services.getLoanPaymentsByApplicationID(db, loan_application_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_item

@LoanPaymentRouter.get("/", response_model=list[LoanPayments])
def read_loan_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.getLoanPayments(db, skip, limit)

@LoanPaymentRouter.post("/disburse")
def disburse_payment(id: int, db: Session = Depends(get_db)):
    return services.disbursePayment(db, id)