from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import engine, Base
from app.models import HCP, Interaction, Material, Sample
from app.routers.hcp_router import router as hcp_router
from app.routers.interaction_router import router as interaction_router
from app.routers.ai_router import router as ai_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI CRM HCP API",
    description="Backend for AI-First CRM HCP Module",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hcp_router)
app.include_router(interaction_router)
app.include_router(ai_router)

@app.get("/")
def home():
    return {"message": "AI CRM Backend Running Successfully"}