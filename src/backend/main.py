from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session
from .database import engine, create_db_and_tables
from .routers import auth, todos
from .config import settings
import uvicorn
from better_auth import Auth
from better_auth.api.fastapi import get_auth_stack

# Create FastAPI app instance
app = FastAPI(
    title=settings.APP_NAME,
    description="TaskMastery - Full-Stack Todo Web Application API",
    version=settings.API_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # Expose headers for auth
    expose_headers=["Access-Control-Allow-Origin"]
)

# Initialize Better Auth
auth = Auth(
    secret=settings.BETTER_AUTH_SECRET,
    database_url=settings.DATABASE_URL
)

# Add Better Auth middleware
auth_stack = get_auth_stack(auth)

# Include routers
app.include_router(auth.router, prefix="/api/v1", tags=["Authentication"])
app.include_router(todos.router, prefix="/api/v1", tags=["Todos"])

@app.on_event("startup")
async def startup_event():
    await create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Welcome to TaskMastery API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)