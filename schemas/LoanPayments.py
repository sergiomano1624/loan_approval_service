from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from schemas.Applications import Applications
class LoanPaymentBase(BaseModel):
    loan_application_id: int
    payment_date: Optional[str] = None
    principal: Optional[str] = None
    interest: Optional[str] = None
    amount: Optional[str] = None
    status: Optional[str] = None

class LoanPaymentCreate(LoanPaymentBase):
    pass
    created_by: str

class LoanPayments(LoanPaymentBase):
    id: int
    created_at: Optional[datetime] = None
    # applicationLoanPayments: Applications
    class Config:
        orm_mode = True
    # created_at: str
    # updated_at: str

class LoanPaymentUpdate(LoanPaymentBase):
    pass
    updated_by: str

class LoanPaymentChangeStatus(BaseModel):
    status: Optional[str] = None
