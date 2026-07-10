from sqlalchemy.orm import Session

from app.models.interaction import Interaction
from app.schemas.interaction_schema import InteractionCreate


def create_interaction(db: Session, interaction: InteractionCreate):

    new_interaction = Interaction(
        hcp_id=interaction.hcp_id,
        interaction_date=interaction.interaction_date,
        interaction_time=interaction.interaction_time,
        interaction_type=interaction.interaction_type,
        attendees=interaction.attendees,
        topics_discussed=interaction.topics_discussed,
        summary=interaction.summary,
        sentiment=interaction.sentiment,
        outcomes=interaction.outcomes,
        follow_up=interaction.follow_up
    )

    db.add(new_interaction)
    db.commit()
    db.refresh(new_interaction)

    return new_interaction


def get_all_interactions(db: Session):

    return db.query(Interaction).all()


def update_interaction(db: Session, interaction_id: int, interaction: InteractionCreate):

    existing_interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not existing_interaction:
        return None

    existing_interaction.hcp_id = interaction.hcp_id
    existing_interaction.interaction_date = interaction.interaction_date
    existing_interaction.interaction_time = interaction.interaction_time
    existing_interaction.interaction_type = interaction.interaction_type
    existing_interaction.attendees = interaction.attendees
    existing_interaction.topics_discussed = interaction.topics_discussed
    existing_interaction.summary = interaction.summary
    existing_interaction.sentiment = interaction.sentiment
    existing_interaction.outcomes = interaction.outcomes
    existing_interaction.follow_up = interaction.follow_up

    db.commit()
    db.refresh(existing_interaction)

    return existing_interaction