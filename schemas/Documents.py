from datetime import datetime
from pydantic import BaseModel
from typing import Optional
class DocumentBase(BaseModel):
    bank_account_id: int
    public_id: Optional[str] = None
    secure_url: Optional[str] = None

class Documents(DocumentBase):
    id: int
    created_at: Optional[datetime]
    class Config:
        orm_mode = True
    # created_at: str
    # updated_at: str

class DocumentUpdate(DocumentBase):
    pass
    updated_by: str

class DocumentChangeStatus(BaseModel):
    status: int

