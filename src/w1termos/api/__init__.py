from fastapi import APIRouter, HTTPException
from w1termos.models import NowResponse
router = APIRouter()


@router.get("/now")
def api_now():
    try:
        response: NowResponse = {}
        return response.model_dump()
    except AssertionError:
        raise HTTPException(404)
