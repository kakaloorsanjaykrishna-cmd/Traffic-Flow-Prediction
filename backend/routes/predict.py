from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from predict import predict_traffic

router = APIRouter()


# ==========================
# Request Model
# ==========================

class TrafficInput(BaseModel):
    road_id: float
    average_speed: float
    congestion_level: float
    weather: float
    temperature: float
    rainfall: float
    holiday: float
    day_of_week: float
    hour_of_day: float


# ==========================
# Prediction Endpoint
# ==========================

@router.post("/predict")
def predict(data: TrafficInput):

    try:

        features = [
            data.road_id,
            data.average_speed,
            data.congestion_level,
            data.weather,
            data.temperature,
            data.rainfall,
            data.holiday,
            data.day_of_week,
            data.hour_of_day,
        ]

        result = predict_traffic(features)

        return {
            "success": True,
            "input": data.dict(),
            "prediction": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )