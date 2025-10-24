from fastapi import APIRouter, HTTPException
from w1termos.sensor import get_async_now, get_sensors
from w1termos.models import NowResponse, DeviceResponse, DevicesResponse
from datetime import datetime, timezone

router = APIRouter()


@router.get("/now")
async def api_now():
    try:
        temperature = await get_async_now()
        response: NowResponse = NowResponse(
            temp=temperature, timestamp=datetime.now(tz=timezone.utc)
        )
        return response.model_dump()
    except AssertionError:
        raise HTTPException(404)


@router.get("/devices")
def api_devices():
    try:
        devices = [
            DeviceResponse(
                name=sensor.name,
                id=sensor.id,
            )
            for sensor in get_sensors()
        ]
        response = DevicesResponse(
            devices=devices, timestamp=datetime.now(tz=timezone.utc)
        )
        return response.model_dump()
    except Exception as e:
        raise HTTPException(500, detail=str(e))
