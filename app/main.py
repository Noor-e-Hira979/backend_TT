# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import engine
from app.db import models

# Import routers
from app.api.v1 import auth, students, progress, recommend, chatbot

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lab Progression API")

# === CORS ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === ROUTERS ===
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(students.router, prefix="/api/v1/students", tags=["Students"])
app.include_router(progress.router, prefix="/api/v1/progress", tags=["Progress"])
app.include_router(recommend.router, prefix="/api/v1/recommend", tags=["Recommend"])

# ⭐ ADD THIS ⭐
app.include_router(chatbot.router, prefix="/api/v1/chatbot", tags=["Chatbot"])

@app.get("/")
def root():
    return {"message": "Backend running successfully 🚀"}
