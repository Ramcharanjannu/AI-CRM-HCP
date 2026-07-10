from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    Time,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_id = Column(Integer, ForeignKey("hcps.id"))

    interaction_date = Column(Date, nullable=False)
    interaction_time = Column(Time, nullable=False)

    interaction_type = Column(String(50), nullable=False)

    attendees = Column(Text)

    topics_discussed = Column(Text)

    summary = Column(Text)

    sentiment = Column(String(50))

    outcomes = Column(Text)

    follow_up = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    hcp = relationship(
        "HCP",
        back_populates="interactions"
    )

    materials = relationship(
        "Material",
        back_populates="interaction",
        cascade="all, delete"
    )

    samples = relationship(
        "Sample",
        back_populates="interaction",
        cascade="all, delete"
    )