from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.core.config import settings
from app.db.session import engine
from app.db import models
from app.db.base import Base
from app.api.v1 import auth
from app.api.v1 import users
from app.api.v1 import ai



# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    This runs BEFORE the app starts accepting requests.
    This is where we handle the DB creation and toggling.
    """
    logger.info("Starting up...")
    
    if settings.RESET_DB_ON_STARTUP:
        logger.info("RESET_DB_ON_STARTUP is True. Dropping all tables...")
        Base.metadata.drop_all(bind=engine)
    
    logger.info("Creating tables if they don't exist...")
    Base.metadata.create_all(bind=engine)
    
    # Here is where we will later call our seed function!
    from app.db.seed import seed_db
    seed_db()
    
    yield # The app runs here
    
    logger.info("Shutting down...")

# Initialize FastAPI with the lifespan manager
app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)

# Set up CORS based on .env
origins = [origin.strip() for origin in settings.ALLOWED_ORIGINS.split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173",
                  "http://localhost:8080", "http://127.0.0.1:8080"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(ai.router, prefix="/api/v1/ai", tags=["AI"])

@app.get("/health", tags=["Health"])
def health_check():
    """Basic health check endpoint."""
    return {"status": "healthy", "project": settings.PROJECT_NAME}

@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")