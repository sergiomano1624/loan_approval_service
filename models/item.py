from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from config.db import Base

class Item(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    created_by = Column(String, nullable = True),
    created_at = Column(DateTime(timezone=True), server_default=func.now()),
    updated_by = Column(String(100), nullable=True),
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now()),
    deleted_by = Column(String(100), nullable=True),
    deleted_at = Column(DateTime(timezone=True), nullable=True)