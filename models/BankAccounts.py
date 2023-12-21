from sqlalchemy import Column, Integer, String, DateTime, TEXT
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.db import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class BankAccounts(Base):
    __tablename__ = "bank_accounts"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, index=True)
    bank_name = Column(String(255))
    bank_code = Column(String(255))
    bank_account_no = Column(String(255))
    bank_account_type = Column(String(255))
    status = Column(String(255), nullable=True)
    created_by = Column(String, nullable = False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_by = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now())
    deleted_by = Column(String, nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # clientUsers = relationship("ClientAdmin", back_populates="clientUsers")
    # recruiterUsers = relationship("RecruiterAdmin", back_populates="recruiter_users")
    # resumeUsers = relationship("Resume", back_populates="resume_users")