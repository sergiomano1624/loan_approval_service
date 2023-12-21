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
    status = Column(String(255))
    created_by = Column(String, nullable = False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_by = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now())
    deleted_by = Column(String, nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # clientUsers = relationship("ClientAdmin", back_populates="clientUsers")
    # recruiterUsers = relationship("RecruiterAdmin", back_populates="recruiter_users")
    # resumeUsers = relationship("Resume", back_populates="resume_users")