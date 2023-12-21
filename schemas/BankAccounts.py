from datetime import datetime
from pydantic import BaseModel
from typing import Optional
class BankAccountBase(BaseModel):
    application_id: int
    bank_name: Optional[str] = None
    bank_code: Optional[str] = None
    bank_account_no: Optional[str] = None
    bank_account_type: Optional[str] = None
    status: Optional[str] = None
    # deleted_by: Optional[str]

class BankAccountCreate(BankAccountBase):
    pass
    created_by: str

class BankAccounts(BankAccountBase):
    id: int
    created_at: Optional[datetime]
    class Config:
        orm_mode = True
    # created_at: str
    # updated_at: str

class BankAccountUpdate(BankAccountBase):
    pass
    updated_by: str

class BankAccountChangeStatus(BaseModel):
    status: Optional[str] = None
