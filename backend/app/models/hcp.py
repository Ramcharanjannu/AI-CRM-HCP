from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base


class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    specialization = Column(String(100), nullable=False)
    hospital = Column(String(150), nullable=False)
    city = Column(String(100), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    interactions = relationship(
        "Interaction",
        back_populates="hcp",
        cascade="all, delete"
    )