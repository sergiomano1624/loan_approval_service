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
    loan_amount: int
    term: int
    interest: int
    repayment_period: int
    trn_no: Optional[str] = None
    monthly_income: int
    secure_url: Optional[str] = None
    date: Optional[str] = None
    amount_offered: int
    type: Optional[str] = None
    comments: Optional[str] = None
    status: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass
    created_by: str

class Applications(ApplicationBase):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        orm_mode = True
    # created_at: str
    # updated_at: str

class ApplicationUpdate(BaseModel):
    date: Optional[str] = None
    amount_offered: Optional[int] = None
    type: Optional[str] = None
    comments: Optional[str] = None
    status: Optional[str] = None
    updated_by: str

class ApplicationChangeStatus(BaseModel):
    status: int

