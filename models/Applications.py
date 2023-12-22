from sqlalchemy import Column, Integer, String, DateTime, TEXT
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.db import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Applications(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    borrower_name = Column(String(255))
    email = Column(String(255))
    address = Column(TEXT)
    mobile = Column(String(100))
    dob = Column(String(100))
    gender = Column(String(100))
    credit_product = Column(String(255))
    loan_amount = Column(String(255))
    term = Column(String(255))
    interest = Column(String(255))
    repayment_period = Column(String(255))
    trn_no = Column(String(255))
    monthly_income = Column(String(255))
    public_id = Column(String(255))
    secure_url = Column(String(255))
    date = Column(String(255), nullable=True)
    amount_offered = Column(String(255), nullable=True)
    type = Column(String(255), nullable=True)
    comments = Column(String(255), nullable=True)
    status = Column(String(255), nullable=True)
    created_by = Column(String, nullable = False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_by = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now())
    deleted_by = Column(String, nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    applicationBankAccounts = relationship("BankAccounts", back_populates="applicationBankAccounts")