from fastapi import APIRouter

router = APIRouter(tags=["Weather"])


@router.get("/weather")
def weather():

    return {

        "temperature": 30,

        "weather": "Sunny",

        "humidity": 62,

        "wind_speed": 14

    }