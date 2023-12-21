from sqlalchemy import Column, Integer, String, DateTime, TEXT
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.db import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class LoanStatus(Base):
    __tablename__ = "loan_status"

    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, index=True)
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

    # clientUsers = relationship("ClientAdmin", back_populates="clientUsers")
    # recruiterUsers = relationship("RecruiterAdmin", back_populates="recruiter_users")
    # resumeUsers = relationship("Resume", back_populates="resume_users")