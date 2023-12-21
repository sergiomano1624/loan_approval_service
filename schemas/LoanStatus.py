from datetime import datetime
from pydantic import BaseModel
from typing import Optional
class LoanStatusBase(BaseModel):
    application_id: int
    date: Optional[str] = None
    amount_offered: Optional[str] = None
    type: Optional[str] = None
    comments: Optional[str] = None
    status: Optional[str] = None

class LoanStatusCreate(LoanStatusBase):
    pass
    created_by: str

class LoanStatus(LoanStatusBase):
    id: int
    created_at: Optional[datetime]
    class Config:
        orm_mode = True
    # created_at: str
    # updated_at: str

class LoanStatusUpdate(LoanStatusBase):
    pass
    updated_by: str

class LoanStatusChangeStatus(BaseModel):
    status: Optional[str] = None
