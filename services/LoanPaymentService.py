from sqlalchemy.orm import Session
from models.Applications import Applications
from models.BankAccounts import BankAccounts
from models.LoanPayments import LoanPayments
from schemas.LoanPayments import LoanPaymentCreate, LoanPaymentUpdate, LoanPaymentChangeStatus
from models.Documents import Documents
from datetime import datetime, timedelta
from cloudinary.uploader import upload
from fastapi import HTTPException
from dateutil.relativedelta import relativedelta


def getLoanPaymentsByApplicationID(db: Session, id: int):
    return db.query(LoanPayments).filter(LoanPayments.loan_application_id == id, LoanPayments.deleted_at.is_(None)).all()
def getLoanPayments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LoanPayments).filter(LoanPayments.deleted_at.is_(None)).offset(skip).limit(limit).all()

def disbursePayment(db: Session, id: int):
    getApplicationById = db.query(Applications).filter(Applications.id == id, Applications.deleted_at.is_(None)).first()

    amountOfferd = int(getApplicationById.amount_offered.replace(",", ""))
    noOfMonths = getApplicationById.term * 12 | 12
    interest = getApplicationById.interest / 100
    totalReturned = amountOfferd + interest

    monthlyFee = totalReturned / noOfMonths

    startDate = getApplicationById.created_at

    for i in range(noOfMonths):
        current_date = startDate + relativedelta(months=i)
        loanPayments = LoanPayments(
            loan_application_id=id,
            payment_date=current_date.date(),
            principal=amountOfferd,
            interest=getApplicationById.interest,
            amount=round(monthlyFee, 2),
            status="Disbursed"
        )
        db.add(loanPayments)
        db.commit()
        db.refresh(loanPayments)

    getApplicationById.status = "Disbursed"
    db.commit()
    db.refresh(getApplicationById)
    return getApplicationById

