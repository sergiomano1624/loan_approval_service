from sqlalchemy import Column, Integer, String, DateTime, TEXT
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.db import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Documents(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    bank_account_id = Column(Integer, index=True)
    public_id = Column(String(255), nullable=True)
    secure_url = Column(String(255))
    created_by = Column(String, nullable = False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_by = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now())
    deleted_by = Column(String, nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # clientUsers = relationship("ClientAdmin", back_populates="clientUsers")
    # recruiterUsers = relationship("RecruiterAdmin", back_populates="recruiter_users")
    # resumeUsers = relationship("Resume", back_populates="resume_users")