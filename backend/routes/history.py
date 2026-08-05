from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import get_db

router = APIRouter(tags=["History"])


@router.get("/history")
def history(db: Session = Depends(get_db)):

    rows = db.execute(text("""
        SELECT
        road_id,
        vehicle_count,
        average_speed,
        congestion_level,
        datetime
        FROM traffic_data
        ORDER BY datetime DESC
        LIMIT 20
    """)).fetchall()

    return [

        {
            "road": row[0],
            "vehicles": row[1],
            "speed": row[2],
            "traffic": row[3],
            "datetime": row[4]
        }

        for row in rows

    ]