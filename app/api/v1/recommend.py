from fastapi import APIRouter
from app.services.recommend_service import get_role_recommendation

router = APIRouter()

@router.post("/")
def recommend(profile: dict):
    return get_role_recommendation(profile)
