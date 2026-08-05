from fastapi import APIRouter

router = APIRouter()

@router.get("/settings")
def get_settings():
    return {
        "theme": "Light",
        "refresh_interval": 5,
        "notifications": True
    }