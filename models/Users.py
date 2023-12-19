from sqlalchemy import Column, Integer, String, DateTime, TEXT
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.db import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    password = Column(String(500))
    gender = Column(String(100))
    email = Column(String(100))
    mobile = Column(String(100))
    user_type = Column(String(255))
    status = Column(Integer)
    last_login = Column(DateTime(timezone=True), nullable=True)
    token = Column(String(255))
    expired_at = Column(String(255))
    created_by = Column(String, nullable = False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_by = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now())
    deleted_by = Column(String, nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # clientUsers = relationship("ClientAdmin", back_populates="clientUsers")
    # recruiterUsers = relationship("RecruiterAdmin", back_populates="recruiter_users")
    # resumeUsers = relationship("Resume", back_populates="resume_users")