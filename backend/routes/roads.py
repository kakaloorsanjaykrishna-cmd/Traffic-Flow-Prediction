from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import get_db

router = APIRouter(tags=["Roads"])


@router.get("/roads")
def roads(db: Session = Depends(get_db)):

    rows = db.execute(text("""
        SELECT DISTINCT road_id
        FROM traffic_data
        ORDER BY road_id
    """)).fetchall()

    return [

        {

            "road_id": row[0]

        }

        for row in rows

    ]