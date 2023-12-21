from sqlalchemy.orm import Session
from models.BankAccounts import BankAccounts
from schemas.BankAccounts import BankAccountCreate, BankAccountUpdate, BankAccountChangeStatus
from models.Documents import Documents
from datetime import datetime
from uuid import UUID
from cloudinary.uploader import upload
from fastapi import HTTPException

def createBankAccount(db: Session, application_id, bank_name, bank_code, bank_account_no, bank_account_type, secure_url, created_by, file):

    checkBankAccountExists = db.query(BankAccounts).filter(BankAccounts.application_id == application_id).first()
    if(checkBankAccountExists):
        db_item = db.query(BankAccounts).filter(BankAccounts.id == application_id).first()
        if db_item:
            db_item.application_id = application_id
            db_item.bank_name = bank_name
            db_item.bank_code = bank_code
            db_item.bank_account_no = bank_account_no
            db_item.bank_account_type = bank_account_type
            db.commit()
            db.refresh(db_item)
            if (file):
                cloudinary_response = upload(file.file)
                docData = Documents(
                    bank_account_id=db_item.id,
                    public_id=cloudinary_response["public_id"],
                    secure_url=cloudinary_response["url"],
                    created_by=created_by)

                db.add(docData)
                db.commit()
                db.refresh(docData)
            return {"message": "Bank account updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
        return db_item
    else:
        bank_account = BankAccounts(
            application_id=application_id,
            bank_name=bank_name,
            bank_code=bank_code,
            bank_account_no=bank_account_no,
            bank_account_type=bank_account_type,
            created_by=created_by)
        db.add(bank_account)
        db.commit()
        db.refresh(bank_account)

        # Store the last insert ID in the "documents" table
        if(file):
            cloudinary_response = upload(file.file)
            docData = Documents(
                bank_account_id=bank_account.id,
                public_id=cloudinary_response["public_id"],
                secure_url=cloudinary_response["url"],
                created_by=created_by)

            db.add(docData)
            db.commit()
            db.refresh(docData)
        return {"message": "Bank account added successfully"}

def getBankAccountByID(db: Session, id: UUID):
    return db.query(BankAccounts).filter(BankAccounts.id == id, BankAccounts.deleted_at.is_(None)).first()
    # return db.query(BankAccounts).filter(BankAccounts.id == id).first()

def getBankAccounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BankAccounts).filter(BankAccounts.deleted_at.is_(None)).offset(skip).limit(limit).all()
    # return db.query(BankAccounts).offset(skip).limit(limit).all()

def changeBankAccountStatus(db: Session, item_id: UUID, req: BankAccountChangeStatus):
    getData = db.query(BankAccounts).filter(BankAccounts.id == item_id).first()
    if getData:
        getData.status = req.status
        db.commit()

def getDocumentByID(db: Session, id: id):
    return db.query(Documents).filter(Documents.id == id, Documents.deleted_at.is_(None)).first()

def deleteDocuments(db: Session, id: id, deleted_by: str):
    db_item = db.query(Documents).filter(Documents.id == id).first()
    if db_item:
        db_item.deleted_at = datetime.now()
        db_item.deleted_by = deleted_by
        db.commit()
