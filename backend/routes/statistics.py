from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import get_db

router = APIRouter(tags=["Statistics"])


@router.get("/statistics")
def statistics(db: Session = Depends(get_db)):

    total = db.execute(
        text("SELECT COUNT(*) FROM traffic_data")
    ).scalar()

    avg_speed = db.execute(
        text("SELECT ROUND(AVG(average_speed),1) FROM traffic_data")
    ).scalar()

    max_vehicle = db.execute(
        text("SELECT MAX(vehicle_count) FROM traffic_data")
    ).scalar()

    return {

        "records": total,

        "average_speed": avg_speed,

        "max_vehicle_count": max_vehicle

    }