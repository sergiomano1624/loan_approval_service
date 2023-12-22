from fastapi import APIRouter, Depends, HTTPException, File, Form, UploadFile
from sqlalchemy.orm import Session
from config import db as database
from services import BankAccountService as services
from schemas.Documents import Documents
from schemas.BankAccounts import BankAccounts, BankAccountCreate, BankAccountUpdate, BankAccountChangeStatus
# from utils.jwt import create_access_token, decode_token
from datetime import timedelta

BankAccountRouter = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@BankAccountRouter.post("/")
def create_bank_account(
        application_id: str = Form(...),
        bank_name: str = Form(...),
        bank_code: str = Form(...),
        bank_account_no: str = Form(...),
        bank_account_type: str = Form(...),
        secure_url: str = Form(...),
        created_by: str = Form(...),
        file: UploadFile = File(None),
        db: Session = Depends(get_db)
):
    return services.createBankAccount(
        db,
        application_id,
        bank_name,
        bank_code,
        bank_account_no,
        bank_account_type,
        secure_url,
        created_by,
        file)

@BankAccountRouter.get("/{id}", response_model=BankAccounts)
def read_BankAccount(id: int, db: Session = Depends(get_db)):
    db_item = services.getBankAccountByID(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_item

@BankAccountRouter.get("/", response_model=list[BankAccounts])
def read_BankAccounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.getBankAccounts(db, skip, limit)

@BankAccountRouter.put("/{id}/status", response_model=BankAccounts)
def change_status(id: int, req: BankAccountChangeStatus, db: Session = Depends(get_db)):
    db_item = services.getBankAccountByID(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    services.changeBankAccountStatus(db, id, req)
    return db_item

@BankAccountRouter.get("/{bank_account_id}/docs", response_model=list[Documents])
def get_docs_by_bank_account_id(bank_account_id: int, db: Session = Depends(get_db)):
    db_item = services.getDocumentByBankAccountID(db, bank_account_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_item

@BankAccountRouter.put("/{id}/docs/delete")
def delete_Document(id: int, deleted_by: str, db: Session = Depends(get_db)):
    db_item = services.getDocumentByID(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    services.deleteDocuments(db, id, deleted_by)
    return {"message": "Document deleted successfully"}
