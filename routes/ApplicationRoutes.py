from fastapi import APIRouter, Depends, HTTPException, Form, UploadFile, File
from sqlalchemy.orm import Session
from config import db as database
from services import ApplicationService as services
from schemas.Applications import ApplicationCreate, ApplicationChangeStatus, Applications, ApplicationUpdate
from uuid import UUID

Applicationrouter = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@Applicationrouter.post("/")
def create_application(
        borrower_name: str = Form(...),
        email: str = Form(...),
        address: str = Form(...),
        mobile: str = Form(...),
        dob: str = Form(...),
        gender: str = Form(...),
        credit_product: str = Form(...),
        loan_amount: str = Form(...),
        term: int = Form(...),
        interest: int = Form(...),
        repayment_period: str = Form(...),
        trn_no: str = Form(...),
        monthly_income: str = Form(...),
        secure_url: str = Form(...),
        created_by: str = Form(...),
        file: UploadFile = File(...), db: Session = Depends(get_db)
):
    return services.createApplication(
        db,
        borrower_name,
        email,
        address,
        mobile,
        dob,
        gender,
        credit_product,
        loan_amount,
        term,
        interest,
        repayment_period,
        trn_no,
        monthly_income,
        secure_url,
        created_by,
        file)
@Applicationrouter.get("/", response_model=list[Applications])
def read_applications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.getApplications(db, skip, limit)

@Applicationrouter.get("/bank_accounts", response_model=list[Applications])
def read_applications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.getApplications(db, skip, limit)

@Applicationrouter.put("/{id}", response_model=Applications)
def update_application(id: int, item: ApplicationUpdate, db: Session = Depends(get_db)):
    db_item = services.getApplicationByID(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return services.updateApplication(db, id, item)

@Applicationrouter.put("/{id}/status", response_model=Applications)
def change_status(id: UUID, req: ApplicationChangeStatus, db: Session = Depends(get_db)):
    db_item = services.getApplicationByID(db, id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Data not found")
    services.changeApplicationStatus(db, id, req)
    return db_item
