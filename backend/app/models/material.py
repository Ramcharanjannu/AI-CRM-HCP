from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)

    interaction_id = Column(
        Integer,
        ForeignKey("interactions.id")
    )

    material_name = Column(String(100))

    interaction = relationship(
        "Interaction",
        back_populates="materials"
    )