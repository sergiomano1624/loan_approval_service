from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    email: Optional[str] = None
    mobile: Optional[str] = None
    user_type: str
    status: Optional[int]
    deleted_by: Optional[str]

class UserCreate(UserBase):
    pass
    created_by: str

class Users(UserBase):
    id: UUID
    class Config:
        orm_mode = True
    # created_at: str
    # updated_at: str

class UserUpdate(UserBase):
    pass
    updated_by: str

class UserChangeStatus(BaseModel):
    status: int
