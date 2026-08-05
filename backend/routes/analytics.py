from fastapi import APIRouter

router = APIRouter()

@router.get("/analytics")
def analytics():
    return {
        "total_predictions": 1200,
        "average_speed": 54.6,
        "high_traffic": 320,
        "medium_traffic": 650,
        "low_traffic": 230,
        "accuracy": 96.8
    }