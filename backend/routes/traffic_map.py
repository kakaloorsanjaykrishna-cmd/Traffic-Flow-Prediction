from fastapi import APIRouter

router = APIRouter(tags=["Traffic Map"])


@router.get("/traffic-map")
def traffic_map():

    return [

        {
            "road": "R101",
            "lat": 13.6288,
            "lng": 79.4192,
            "traffic": "Medium"
        },

        {
            "road": "R102",
            "lat": 13.6335,
            "lng": 79.4204,
            "traffic": "Low"
        },

        {
            "road": "R103",
            "lat": 13.6204,
            "lng": 79.4282,
            "traffic": "High"
        }

    ]