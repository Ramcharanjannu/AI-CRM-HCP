from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.interaction_schema import (
    InteractionCreate,
    InteractionResponse
)
from app.services.interaction_service import (
    create_interaction,
    get_all_interactions,
    update_interaction
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"]
)


@router.post("/", response_model=InteractionResponse)
def add_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db)
):
    return create_interaction(db, interaction)


@router.get("/", response_model=List[InteractionResponse])
def list_interactions(
    db: Session = Depends(get_db)
):
    return get_all_interactions(db)


@router.put("/{interaction_id}", response_model=InteractionResponse)
def edit_interaction(
    interaction_id: int,
    interaction: InteractionCreate,
    db: Session = Depends(get_db)
):

    updated = update_interaction(
        db,
        interaction_id,
        interaction
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found"
        )

    return updated