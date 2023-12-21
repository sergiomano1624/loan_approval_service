from sqlalchemy.orm import Session
from models.Applications import Applications
from schemas.Applications import ApplicationCreate, ApplicationChangeStatus
from datetime import datetime
from uuid import UUID
from passlib.context import CryptContext
from cloudinary.uploader import upload

def createApplication(db: Session, borrower_name, email, address, mobile, dob, gender, credit_product, loan_amount, term, interest, repayment_period, trn_no, monthly_income, secure_url, created_by,  file):

    cloudinary_response = upload(file.file)

    users = Applications(
        borrower_name=borrower_name,
        email=email,
        address=address,
        mobile=mobile,
        dob=dob,
        gender=gender,
        credit_product=credit_product,
        loan_amount=loan_amount,
        term=term,
        interest=interest,
        repayment_period=repayment_period,
        trn_no=trn_no,
        monthly_income=monthly_income,
        public_id='',
        secure_url=cloudinary_response["url"],
        created_by=created_by)
    db.add(users)
    db.commit()
    db.refresh(users)
    return users

def getApplicationByID(db: Session, id: UUID):
    return db.query(Applications).filter(Applications.id == id, Applications.deleted_at.is_(None)).first()

def getApplications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Applications).filter(Applications.deleted_at.is_(None)).offset(skip).limit(limit).all()

def changeApplicationStatus(db: Session, item_id: UUID, req: ApplicationChangeStatus):
    getData = db.query(Applications).filter(Applications.id == item_id).first()
    if getData:
        getData.status = req.status
        db.commit()
