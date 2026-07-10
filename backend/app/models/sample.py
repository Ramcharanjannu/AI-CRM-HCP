from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True, index=True)

    interaction_id = Column(
        Integer,
        ForeignKey("interactions.id")
    )

    sample_name = Column(String(100))

    quantity = Column(Integer)

    interaction = relationship(
        "Interaction",
        back_populates="samples"
    )