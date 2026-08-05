from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/system-status")
def system_status():

    return {

        "backend": "Online",

        "database": "Connected",

        "model": "Loaded",

        "version": "3.0"

    }