from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
class ApplicationBase(BaseModel):
    borrower_name: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    mobile: Optional[str] = None
    dob: Optional[str] = None
    gender: Optional[str] = None
    credit_product: Optional[str] = None
    loan_amount: Optional[str] = None
    term: Optional[str] = None
    interest: Optional[str] = None
    repayment_period: Optional[str] = None
    trn_no: Optional[str] = None
    monthly_income: Optional[str] = None
    secure_url: Optional[str] = None
    status: Optional[str] = None
    deleted_by: Optional[str]

class ApplicationCreate(ApplicationBase):
    pass
    created_by: str

class Applications(ApplicationBase):
    id: int
    created_at: Optional[datetime]
    class Config:
        orm_mode = True
    # created_at: str
    # updated_at: str

# class ApplicationUpdate(ApplicationBase):
#     pass
#     updated_by: str

class ApplicationChangeStatus(BaseModel):
    status: int

